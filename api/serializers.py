from accounts.models CustomUser

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
