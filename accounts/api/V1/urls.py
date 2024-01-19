from django.urls import path, include
from .views import *


app_name = 'api-v1-accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name = 'registration'),
]
