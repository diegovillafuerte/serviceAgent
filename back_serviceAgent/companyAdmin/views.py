from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from companyAdmin.utils.functionManager import create_function, create_function_set
from django.contrib.auth import authenticate
from companyAdmin.models import Function, Parameter, CompanyUser
from rest_framework.authtoken.models import Token


class CreateFunctionView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            schema = request.data.get('schema')
            company_user_id = request.data.get('company_user_id')

            if schema is None or company_user_id is None:
                return Response({'error': 'Missing required data'}, status=status.HTTP_400_BAD_REQUEST)

            create_function(schema, company_user_id)

            return Response(status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class GetFunctionView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            company_user_id = request.query_params.get('company_user_id')

            if company_user_id is None:
                return Response({'error': 'Missing required data'}, status=status.HTTP_400_BAD_REQUEST)

            function_set = create_function_set(company_user_id)

            return Response(function_set, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            if username is None or password is None:
                return Response({'error': 'Please provide both username and password.'}, 
                                status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, 
                                status=status.HTTP_200_OK)
            else:
                raise ValueError

        except CompanyUser.DoesNotExist:
            raise ValueError
        except ValueError:
            return Response({'error': 'Invalid credentials'}, 
                            status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': 'Something went wrong'}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)