from django.urls import path
from . import api_views

app_name = 'api-articles'

urlpatterns = [
    path('',api_views.articles.as_view(),name='articles'),
    path('search/',api_views.articles_search.as_view(),name='articles_search'),
    path('filter/<int:categoryID>/',api_views.articles_filter_category.as_view(),name='articles_filter_category'),
    path('article-detail/<int:id>/',api_views.articles_detail.as_view(),name='articles_detail'),
    path('categories/', api_views.categories.as_view(), name='categories'),
    path('categories/', api_views.categories.as_view(), name='categories'),
    path('category-detail/<int:id>/', api_views.category_detail.as_view(), name='category_detail'),
]