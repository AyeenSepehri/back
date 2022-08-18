from rest_framework import serializers
from .models import *


class LoginSeriazliers(serializers.Serializer):
    phone = serializers.CharField(max_length=999, required=True)
    code = serializers.CharField(max_length=999, required=True)


class CodesSeriazliers(serializers.Serializer):
    phone = serializers.CharField(max_length=999,required=True)



class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Userperson
        fields = ['phone','image','address']
