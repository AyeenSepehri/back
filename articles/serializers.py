from rest_framework import serializers
from .models import *



class ArticlesSerialziers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Articles
        fields = '__all__'


class CategoriesSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'