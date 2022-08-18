from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from extensions.sms import send_sms
from rest_framework import generics,status
from .serializers import *
from random import randint
from .models import *



class login(generics.CreateAPIView):
    serializer_class = LoginSeriazliers

    def create(self, request, *args, **kwargs):
        data = LoginSeriazliers(data=self.request.data)
        if data.is_valid():
            user = Userperson.objects.filter(phone=request.data['phone']).first()
            if user is not None:
                code = Codes.objects.filter(code=request.data['code'],user_id=user.id).first()
                if code is not None:
                    token = Token.objects.filter(user_id=user.id).first()
                    if token is  None:
                        token = Token.objects.create(user_id=user.id)
                    else: pass

                    code.delete()

                    return Response({'token': token.key})

                else:
                    return Response({'message': 'کد تایید اشتباه است'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'کاربر ثبت نشده است'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)



class send_code(generics.CreateAPIView):
    serializer_class = CodesSeriazliers

    def create(self, request, *args, **kwargs):
        data = CodesSeriazliers(data=self.request.data)
        if data.is_valid():
            phone = self.request.data['phone']
            user = Userperson.objects.filter(phone=phone).first()
            if user is not None:
                codes = Codes.objects.filter(user_id=user.id).all()
                codes.delete()
                code = randint(1000,60000)
                code_create = Codes.objects.create(code=code,user_id=user.id)
                send_sms(phone,f"Code:{code}\n\nکد تایید شما")
                return Response({'message': 'کد تایید ارسال شد'})
            else:
                return Response({'message': 'کاربر ثبت نشده است'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data.errors)




class register(generics.CreateAPIView):
    serializer_class = UsersSerializers
    queryset = Userperson.objects.all()

