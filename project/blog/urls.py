from django.urls import path
from .views import category_list, category_detail, product_list, product_detail

app_name = 'blog'

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/<int:category_id>/', category_detail, name='category_detail'),
    path('categories/<int:category_id>/products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
]
