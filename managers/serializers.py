from products.models import Products,Categories,Trackings
from usersmodel.models import Userperson
from rest_framework import serializers
from settings.models import Settings

class SettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'


class UsersSerialziers(serializers.ModelSerializer):
    class Meta:
        model = Userperson
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'



class NewslettersSerializers(serializers.Serializer):
    subject = serializers.CharField(max_length=999,required=True)
    message = serializers.CharField(max_length=1000000,required=True)
    




class TrackingsSerializers(serializers.Serializer):
    class Meta:
        model = Trackings
        fields = '__all__'
