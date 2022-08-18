from rest_framework import serializers
from .models import *


class TiketsSerializers(serializers.ModelSerializer):
    customer = serializers.IntegerField(required=False)
    support = serializers.IntegerField(required=False)
    class Meta:
        model = Tikets
        fields = '__all__'



class MessagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('file') == None and  attrs.get('text') == None:
            raise serializers.ValidationError({'message': 'plz Send Text or File'})
        else:
            return attrs

