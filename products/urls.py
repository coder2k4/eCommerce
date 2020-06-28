from django.urls import path

from products.views import ProductListView, ProductDetailSlugView

app_name = 'Products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<str:slug>', ProductDetailSlugView.as_view(), name='detail'),
]
