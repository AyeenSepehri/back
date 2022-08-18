from django.urls import path
from . import api_views

app_name = 'api-usersmodel'

urlpatterns = [
    path('login/',api_views.login.as_view(),name='login'),
    path('send-code/',api_views.send_code.as_view(),name='send_code'),
    path('register/',api_views.register.as_view(),name='register'),
]