from django.shortcuts import render
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import CreateUserSerializer , UserSerializer
from rest_framework import viewsets , permissions , generics

# Create your views here.


class RegistrationAPI(generics.GenericAPIView):
    serializer_class  = CreateUserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_excpetion=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })