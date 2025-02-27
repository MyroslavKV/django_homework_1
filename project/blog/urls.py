from django.urls import path
from .views import category_list, product_list
app_name = 'blog'

urlpatterns = [
    path('categories/', category_list, name='categories'), 
    path('products/', product_list, name='products'), 
]
