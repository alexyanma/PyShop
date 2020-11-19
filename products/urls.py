from django.urls import path
# . means current folder
# import views model from current folder
from . import views


# current package is /products --> '', means all url will start with /products
# /products/1/details
# /products/new
urlpatterns = [
    path('', views.index),
    path('new', views.new_products)
]
