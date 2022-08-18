from django.urls import path
from . import api_views

app_name = 'api-customers'

urlpatterns = [
    # tiket and messages
    path('tikets/',api_views.tikets.as_view(),name='tikets'),
    path('tiket-create/',api_views.tiket_create.as_view(),name='tiket_create'),
    path('messages/',api_views.messages.as_view(),name='messages'),

]