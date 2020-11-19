from django.http import HttpResponse
from .models import Product
# django is package, shortcuts is model and render is function
from django.shortcuts import render
# index is main page

# mapping /products --> index


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_products(request):
    return HttpResponse('New Products')
