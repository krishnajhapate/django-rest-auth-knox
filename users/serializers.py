from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id','username','password')
        extra_kwargs = {'passowrd':{'write_only':True}}

    def create(self,validate_data):
        user = User.objects.create_user(validate_data['username'],None,validate_data['password'])
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')