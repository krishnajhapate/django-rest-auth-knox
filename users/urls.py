from django.urls import path
from .views import RegistrationAPI,LoginAPI,UserAPI

urlpatterns = [
    path('registration/',RegistrationAPI.as_view(),name="registration"),
    path('login/',LoginAPI.as_view(),name="login"),
    path('user/',UserAPI.as_view(),name="user"),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')
]