from django.urls import path
from companyAdmin.utils.urls import CreateFunctionView, GetFunctionView, LoginView

urlpatterns = [
    path('create_function/', CreateFunctionView.as_view(), name='create_function'),
    path('get_functions/', GetFunctionView.as_view(), name='get_functions'),
    path('login/', LoginView.as_view(), name='login'),
]