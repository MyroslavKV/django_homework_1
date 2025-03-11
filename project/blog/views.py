from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    if not categories:
        messages.warning(request, "No categories available.")
    return render(request, "categories.html", {"categories": categories})

def product_list(request):
    products = Product.objects.all()
    if not products:
        messages.warning(request, "No products available.")
    return render(request, "products.html", {"products": products})