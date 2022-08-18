from django.urls import path
from . import api_views

app_name = 'api-managers'

urlpatterns = [
    # settings
    path('settings/',api_views.settings.as_view(),name='settings'),
    path('setting-create/',api_views.setting_create.as_view(),name='setting_create'),
    path('setting-detail/<int:id>/',api_views.setting_detail.as_view(),name='setting_detail'),
    path('setting-update/<int:id>/',api_views.setting_update.as_view(),name='setting_update'),
    path('setting-delete/<int:id>/',api_views.setting_delete.as_view(),name='setting_delete'),
    # users
    path('users/',api_views.users.as_view(),name='users'),
    path('user-create/<int:id>/',api_views.user_create.as_view(),name='user_create'),
    path('user-detail/<int:id>/',api_views.user_detail.as_view(),name='user_detail'),
    path('user-update/<int:id>/',api_views.user_update.as_view(),name='user_update'),
    path('user-delete/<int:id>/',api_views.user_delete.as_view(),name='user_delete'),
    # products
    path('products/', api_views.products.as_view(), name='products'),
    path('product-create/<int:id>/', api_views.product_create.as_view(), name='product_create'),
    path('product-detail/<int:id>/', api_views.product_detail.as_view(), name='product_detail'),
    path('product-update/<int:id>/', api_views.product_update.as_view(), name='product_update'),
    path('product-delete/<int:id>/', api_views.product_delete.as_view(), name='product_delete'),
    # categories
    path('categories/', api_views.categories.as_view(), name='categories'),
    path('category-create/<int:id>/', api_views.category_create.as_view(), name='category_create'),
    path('category-detail/<int:id>/', api_views.category_detail.as_view(), name='category_detail'),
    path('category-update/<int:id>/', api_views.category_update.as_view(), name='category_update'),
    path('category-delete/<int:id>/', api_views.category_delete.as_view(), name='category_delete'),
    # newsletters
    path('newsletters-send/', api_views.newsletters_send.as_view(), name='newsletters_send'),
    # trackings
    path('trackings/', api_views.trackings.as_view(), name='trackings'),
    path('tracking-create/<int:id>/', api_views.tracking_create.as_view(), name='tracking_create'),
    path('tracking-detail/<int:id>/', api_views.tracking_detail.as_view(), name='tracking_detail'),
    path('tracking-update/<int:id>/', api_views.tracking_update.as_view(), name='tracking_update'),
    path('tracking-delete/<int:id>/', api_views.tracking_delete.as_view(), name='tracking_delete'),

]
