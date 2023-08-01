from companyAdmin.models import Function, Parameter, CompanyUser
from django.shortcuts import get_object_or_404
from django.db import transaction
import json
from django.forms.models import model_to_dict

@transaction.atomic
def create_function(schema, company_user_id):
    '''
    Creates a new function object with the given schema and company user ID.

    Args:
        schema (dict): A dictionary containing the schema for the new function.
            The schema should include the following keys:
            - name (str): The name of the function.
            - description (str): A description of the function.
            - endpoint (str): The endpoint for the function.
            - parameters (dict): A dictionary containing the parameters for the function.

        company_user_id (int): The ID of the company user that the function belongs to.

    Returns:
        None
    '''
    company_user = get_object_or_404(CompanyUser, id=company_user_id)

    Function.objects.create(
        name=schema["name"],
        description=schema["description"],
        endpoint=schema["endpoint"],
        company=company_user,
        parameters=json.dumps(schema['parameters'])
    )

def model_to_json(model):
    '''
    Converts a Django model to a JSON object.

    Args:
        model (django.db.models.Model): The Django model to convert.

    Returns:
        dict: A dictionary representing the JSON object.
    '''
    # Use model_to_dict to convert most fields
    function_dict = model_to_dict(model, exclude=['parameters', 'endpoint'])
    
    # Manually convert parameters
    function_dict['parameters'] = Function._meta.get_field('parameters').value_from_object(model)

    return function_dict
    
def create_function_set(company_user_id):
    '''
    Creates a list of function dictionaries for the given company user ID. This is formatted as the input for the GPT-4 API. 

    Args:
        company_user_id (int): The ID of the company user.

    Returns:
        list: A list of dictionaries representing the functions for the company user.
            Each dictionary should include the following keys:
            - id (int): The ID of the function.
            - name (str): The name of the function.
            - description (str): A description of the function.
            - parameters (str): A JSON string representing the parameters for the function.
    '''
    company_user = get_object_or_404(CompanyUser, id=company_user_id)

    function_dicts = []

    for function in company_user.functions.all():
        function_dict = model_to_json(function)
        function_dicts.append(function_dict)

    return function_dicts

def create_function_map(company_user_id):
    '''
    Creates a dictionary mapping function names to endpoints for the given company user ID.

    Args:
        company_user_id (int): The ID of the company user.

    Returns:
        dict: A dictionary where the keys are the function names and the values are the endpoints.
    '''
    # Get the Function objects for a specific company user
    company_functions = Function.objects.filter(company__id=company_user_id)

    # Create a dictionary where the keys are the function names and the values are the endpoints
    function_map = {func.name: func.endpoint for func in company_functions}

    return function_map


    


   
