from django.urls import path
from . import api_views

app_name = 'api-newsletters'


urlpatterns = [
    path('newsletters/',api_views.newsletters.as_view(),name='newsletters'),
    path('newsletter-create/',api_views.newsletter_create.as_view(),name='newsletter_create'),
]