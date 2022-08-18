from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    # payment
    path('payment/request/', views.send_request, name='send_request'),
    path('payment/verify/', views.verify, name='verify'),
]