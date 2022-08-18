from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('wallet/request/<str:price>/', views.wallet_send_request, name='wallet_send_request'),
    path('wallet/verify/', views.wallet_verify, name='wallet_verify'),
]