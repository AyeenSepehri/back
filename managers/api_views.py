from config.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import generics,status
from email.message import EmailMessage
from newsletters.models import Newsletters
from .serializers import *
from .serializers import *
import smtplib


class settings(generics.ListAPIView):
    """
     Show Settings List
    """
    serializer_class = SettingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Settings.objects.all()



class setting_create(generics.CreateAPIView):
    """
     Create Setting
    """
    serializer_class = SettingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Settings.objects.all()


class setting_detail(generics.ListAPIView):
    """
     Show Setting Detail
    """
    serializer_class = SettingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Settings.objects.all()
    lookup_field = 'id'


class setting_update(generics.UpdateAPIView):
    """
     Update Setting info
    """
    serializer_class = SettingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Settings.objects.all()
    lookup_field = 'id'



class setting_delete(generics.DestroyAPIView):
    """
     Delete Setting
    """
    serializer_class = SettingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Settings.objects.all()
    lookup_field = 'id'





class users(generics.ListAPIView):
    """
     Show Users List
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()



class user_create(generics.CreateAPIView):
    """
     Create User
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()


class user_detail(generics.ListAPIView):
    """
     Show User Detail
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()
    lookup_field = 'id'


class user_update(generics.UpdateAPIView):
    """
     Update User info
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()
    lookup_field = 'id'



class user_delete(generics.DestroyAPIView):
    """
     Delete User
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()
    lookup_field = 'id'








class products(generics.ListAPIView):
    """
     Show Products List
    """
    serializer_class = ProductsSerializers
    permission_classes = [IsAdminUser]
    queryset = Products.objects.all()



class product_create(generics.CreateAPIView):
    """
     Create Product
    """
    serializer_class = UsersSerialziers
    permission_classes = [IsAdminUser]
    queryset = Userperson.objects.all()


class product_detail(generics.ListAPIView):
    """
     Show Product Detail
    """
    serializer_class = ProductsSerializers
    permission_classes = [IsAdminUser]
    queryset = Products.objects.all()
    lookup_field = 'id'


class product_update(generics.UpdateAPIView):
    """
     Update Product info
    """
    serializer_class = ProductsSerializers
    permission_classes = [IsAdminUser]
    queryset = Products.objects.all()
    lookup_field = 'id'



class product_delete(generics.DestroyAPIView):
    """
     Delete Product
    """
    serializer_class = ProductsSerializers
    permission_classes = [IsAdminUser]
    queryset = Products.objects.all()
    lookup_field = 'id'





class categories(generics.ListAPIView):
    """
     Show Categories List
    """
    serializer_class = CategoriesSerializers
    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()



class category_create(generics.CreateAPIView):
    """
     Create Category
    """
    serializer_class = CategoriesSerializers
    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()


class category_detail(generics.ListAPIView):
    """
     Show Category Detail
    """
    serializer_class = CategoriesSerializers
    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()
    lookup_field = 'id'


class category_update(generics.UpdateAPIView):
    """
     Update Category info
    """
    serializer_class = CategoriesSerializers
    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()
    lookup_field = 'id'



class category_delete(generics.DestroyAPIView):
    """
     Delete Category
    """
    serializer_class = CategoriesSerializers
    permission_classes = [IsAdminUser]
    queryset = Categories.objects.all()
    lookup_field = 'id'





class newsletters_send(generics.CreateAPIView):
    """
     Newsletters Send
    """
    serializer_class = NewslettersSerializers
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = NewslettersSerializers(data=request.data)
        if data.is_valid():
            try:
                newsletters = Newsletters.objects.all()
                msg = EmailMessage()
                msg['Subject'] = f"{self.request.data['subject']}"
                msg['From'] = EMAIL_HOST_USER
                msg['To'] = f','.join([newsletter.email for newsletter in newsletters])
                msg.set_content(f'{self.request.data["message"]}')
                with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
                    server.login(EMAIL_HOST_USER, EMAIL_HOST_PAASWORD)
                    server.send_message(msg)
                    return Response({'message': 'Emails Send'})
            except:
                return Response({'message': 'ERROR'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)








class trackings(generics.ListAPIView):
    """
     Show Trackings List
    """
    serializer_class = TrackingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Trackings.objects.all()



class tracking_create(generics.CreateAPIView):
    """
     Create Tracking
    """
    serializer_class = TrackingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Trackings.objects.all()


class tracking_detail(generics.ListAPIView):
    """
     Show Tracking Detail
    """
    serializer_class = TrackingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Trackings.objects.all()
    lookup_field = 'id'


class tracking_update(generics.UpdateAPIView):
    """
     Update Tracking info
    """
    serializer_class = TrackingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Trackings.objects.all()
    lookup_field = 'id'



class tracking_delete(generics.DestroyAPIView):
    """
     Delete Tracking
    """
    serializer_class = TrackingsSerializers
    permission_classes = [IsAdminUser]
    queryset = Trackings.objects.all()
    lookup_field = 'id'


