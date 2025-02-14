from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product

def category_list(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        category.delete()
        messages.success(request, f'Catagory was deleteed')
        return redirect("category_list")

    return render(request, "category_detail.html", {"category": category})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "products.html", {"category": category, "products": products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":  
        product.delete()
        messages.success(request, f'product was deleted')
        return redirect("category_list")

    return render(request, "product_detail.html", {"product": product})