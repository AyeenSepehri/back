from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics,status
from .serializers import *
from .models import *



class newsletters(generics.ListAPIView):
    """
     Show Newsletters List
    """
    serializer_class = NewslettersSerializers
    queryset = Newsletters.objects.all()

class newsletter_create(generics.CreateAPIView):
    """
     Create Newsletter
    """
    serializer_class = NewslettersSerializers
    queryset = Newsletters.objects.all()