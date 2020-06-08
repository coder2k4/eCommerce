from django.urls import path

from cart.views import cart_home, cart_update, checkout_home, checkout_done_view, cart_detail_api_view

app_name = "cart"

urlpatterns = [
    path('', cart_home, name='home'),
    path('api/', cart_detail_api_view, name='api'),
    path('update/', cart_update, name='update'),
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/success/', checkout_done_view, name='success'),
]
