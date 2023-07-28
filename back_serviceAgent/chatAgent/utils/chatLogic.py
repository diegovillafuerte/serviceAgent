import chatAgent.utils.gpt as gpt
from chatAgent.models import ClientUser, Conversation, Message
from chatAgent.utils import functionList
import json
from rest_framework import status
import datetime


def create_context(userClient, userCompany):
    '''
    This functions checks if the userClient has had past conversations with the userCompany and if so, it will create a context for the conversation.
    '''
    return None

def conversational_agent(message, userClient, userCompany):
    """
    This function works as the brains of the chatbot that gives service to the client user.

    It first receives the message, and checks if the user is in active conversation or if this is the first message

    If its the first message it creates a new conversation assigned to the user and saves the new message to the database

    It then creates a list with history of the conversation starting by the system prompt and then the messages in the conversation in chronological order using the following format:
                history.append({
                        "role": "user",
                        "content": human_input
                    })

                     history.append({
                        "role": "assistant",
                        "content": response_message["content"]
                    })

    It then sends the history to the gpt function to generate a response. 

    If the response is a function call, it will call the relevant function and send the response to the user.

    If the response is not a function call, it will log the message to the conversation in the database and then send the response to the user.
    """


    
    system_prompt = [
    {
        "role": "system",
        "content": (
            f"You are a super-inteligent and friendly customer service representative for {userCompany.user.username}. "
            "Your only job is to help the user find whatever they are looking in the context of the company. You politely refuse to answer anything not related to the company."
            "You always do your best to do right by the customer and providing a delightful experience within the limits of your capabilities is your top priority."
            "Remember to be really friendly and refer to the user by their first name. If you don't know their name, you should politely ask for it."
            f"Remember that the current date is {datetime.datetime.now()}."
            "If the user speaks in another language, you should continue the conversation in that language."
    )}]

    # Check if the user has had previous conversations with the company and if so, create a context to add to this interaction
    context = create_context(userClient, userCompany)

    if context is not None:
        system_prompt.append({
            "role": "system",
            "content": (
                "Enclosed in -- below is the context of previous interactions that this user has had with this company"
                "It is of the upmost importnace that you read this context and take it into account when responding to the user."
                f"Context: --{context}--"
                )
        })
       
    # Check if the user is in a conversation
    if userClient.current_conversation is None:
        # If not, create a new conversation
        conversation = Conversation.objects.create(clientUser=userClient, status='active')
        userClient.current_conversation = conversation
        userClient.save()
 
    else:
        # If so, get the existing conversation
        conversation = Conversation.objects.get(id=userClient.current_conversation.id)
    
    # Save the new message to the database
    Message.objects.create(
        conversation=conversation,
        sender='user',
        text=message
    )

    # Get the history of the conversation
    history = system_prompt
    messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
    for message in messages:
        history.append({
            "role": message.sender,
            "content": message.text
        })
    
    # Generate a response
    response = gpt.call_gpt(history, functions=functionList.sample_function_set)
    response_message = response["choices"][0]["message"]

    # Check if the response is a function call
    function_chosen = response_message.get("function_call")
    if function_chosen is not None:
        # Get the arguments for the function call
        print(function_chosen)
        #Call the function
        function_name = response_message["function_call"]["name"]
        function_to_call = functionList.function_map.get(function_name)
        function_args = json.loads(response_message["function_call"]["arguments"])
         # Check if the arguments are a dictionary. If so, unpack them.
        if isinstance(function_args, dict):
            response_text = function_to_call(**function_args)
        else:
            response_text = function_to_call(*function_args)

        Message.objects.create(
        conversation=conversation,
        sender='assistant',
        text=response_text
        )

    else:
        # Log the message to the conversation in the database
        response_text = response_message['content']
        Message.objects.create(
            conversation=conversation,
            sender='assistant',
            text=response_text
        )
    print(response_text)
    return {"result": response_text}, status.HTTP_200_OK

def finish_conversation(clientUser, companyUser):
    """
    This function is called when the user wants to end the conversation.
    It will set the conversation status to finished and set the current conversation of the user to None
    """
        #This resets the current conversation for the user to null and sets the conversation's status to finished
    if clientUser.current_conversation is not None: 
        conversation = clientUser.current_conversation
        conversation.status = 'finished'
        conversation.save()
        clientUser.current_conversation = None
        clientUser.save()
    return None

