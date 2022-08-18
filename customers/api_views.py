from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics,status
from .serializers import *
from .models import *


class tikets(generics.ListAPIView):
    serializer_class = TiketsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tikets.objects.filter(customer_id=self.request.user.id).all()




class tiket_create(generics.CreateAPIView):
    serializer_class = TiketsSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = TiketsSerializers(data=request.data)
        if data.is_valid():
            tiket = Tikets.objects.create(customer_id=self.request.user.id)
            return Response({'message': f'تیکت با موفقیت ساخته شد '})
        else:
            return Response(data.errors)


class messages(generics.CreateAPIView):
    serializer_class = MessagesSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = MessagesSerializers(data=request.data)
        if data.is_valid():
            data.save()
            data.instance.role = 'customer'
            data.save()
            return Response({'message': f'پیام با موفقیت اضافه شد'})
        else:
            return Response(data.errors)