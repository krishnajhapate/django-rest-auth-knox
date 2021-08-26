from django.urls import path
from .views import RegistrationAPI

urlpatterns = [
    path('registration/',RegistrationAPI.as_view(),name="registration")
]