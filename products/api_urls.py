from django.urls import path
from . import api_views

app_name = 'api-products'


urlpatterns = [
    # products
    path('',api_views.products.as_view(),name='products'),
    path('search/',api_views.products_search.as_view(),name='products_search'),
    path('filter-category/<int:categoryID>/',api_views.products_filter_category.as_view(),name='products_filter_category'),
    path('product-detail/<int:id>/',api_views.product_detail.as_view(),name='product_detail'),
    path('comments/<int:id>/',api_views.product_comments.as_view(),name='product_comments'),
    path('comment-create/<int:id>/',api_views.product_comment_create.as_view(),name='product_comment_create'),
    path('likes/<int:id>/',api_views.product_likes.as_view(),name='product_likes'),
    path('dislikes/<int:id>/',api_views.product_dislikes.as_view(),name='product_dislikes'),
    path('like-create/<int:id>/',api_views.product_like_create.as_view(),name='product_like_create'),
    path('sliders/',api_views.products_sliders.as_view(),name='products_sliders'),
    # categories
    path('categories/',api_views.categories.as_view(),name='categories'),
    path('category-detail/<int:id>/',api_views.category_detail.as_view(),name='category_detail'),
    # carts
    path('carts/',api_views.carts.as_view(),name='carts'),
    path('cart-create/<int:id>/',api_views.cart_create.as_view(),name='cart_delete'),
    path('cart-delete/<int:id>/',api_views.cart_delete.as_view(),name='cart_delete'),
    # tracking
    path('tracking/<str:code>/', api_views.tracking.as_view(), name='tracking'),
]