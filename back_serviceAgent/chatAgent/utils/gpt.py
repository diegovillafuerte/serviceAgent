import openai
import traceback

def call_gpt(prompt, functions=None, model="gpt-4-0613", temperature=0, function_call='auto'):
    """
    Generates a response from the OpenAI GPT model.

    Args:
        prompt (str): The input prompt for the GPT model.
        functions (list, optional): A list of functions to be used in the GPT model. Defaults to None.
        model (str, optional): The name of the GPT model to be used. Defaults to "gpt-4-0613".
        temperature (float, optional): The randomness of the GPT model's output. A higher temperature value will result in more random output. Defaults to 0.
        function_call (str, optional): The function call type. If set to "auto", the function will automatically determine whether to use the provided functions or not. Defaults to 'auto'.

    Returns:
        dict: The response from the GPT model.

    Raises:
        Exception: If an exception occurs, the function will print the traceback.
    """
    try:
        if functions is None:
            response = openai.ChatCompletion.create(
                model=model,
                messages=prompt,
                temperature=temperature
            )
        else:
            response = openai.ChatCompletion.create(
                model=model,
                functions=functions,
                messages=prompt,
                temperature=temperature,
                function_call=function_call
            )
        return response
    except Exception as e:
        traceback.print_exc()
