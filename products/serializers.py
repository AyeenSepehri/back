from rest_framework import serializers
from .models import *

class ProductsSerialziers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Products
        fields = '__all__'


class CategoriesSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CommentsSerialziers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Comments
        fields = '__all__'

class LikesSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class SlidersSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = '__all__'


class OrdersSerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    descriptions = serializers.CharField(required=False)
    count = serializers.IntegerField(required=True)
    class Meta:
        model = Orders
        fields = '__all__'


class TrackingsSerializers(serializers.ModelSerializer):
    orders = serializers.ReadOnlyField()
    class Meta:
        model = Trackings
        fields = '__all__'