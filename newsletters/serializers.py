from rest_framework import serializers
from .models import *



class NewslettersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Newsletters
        fields = '__all__'