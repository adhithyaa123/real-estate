from rest_framework import serializers
from api.models import Property
from django.contrib.auth.models import User


class PropertySerializer(serializers.ModelSerializer):

    class Meta:

        model=Property

        fields="__all__"


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["username","email","password"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data) 

