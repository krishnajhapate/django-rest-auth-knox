from django.urls import path
from .views import RegistrationAPI,LoginAPI

urlpatterns = [
    path('registration/',RegistrationAPI.as_view(),name="registration"),
    path('Login/',LoginAPI.as_view(),name="login"),
]