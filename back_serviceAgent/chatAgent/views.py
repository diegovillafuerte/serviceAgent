from rest_framework import status
from rest_framework.response import Response
from chatAgent.models import Message, Conversation, ClientUser
from companyAdmin.models import CompanyUser
from chatAgent.utils.chatLogic import conversational_agent
from rest_framework.views import APIView

class ChatView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        message_text = request.data.get('message')
        company_user_id = request.data.get('companyUser_id') 

        try:
            # get the company user
            company_user = CompanyUser.objects.get(id=company_user_id)
        except CompanyUser.DoesNotExist:
            return Response({"error": "CompanyUser does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # get the client user based on the email provided in the request, create if not exist
        client_user, created = ClientUser.objects.get_or_create(email=email, company=company_user)

        # call the conversational_agent function and get the response
        response, status_code = conversational_agent(message_text, client_user, company_user)

        return Response(response, status=status_code)
