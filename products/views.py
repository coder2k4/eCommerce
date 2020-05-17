from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
