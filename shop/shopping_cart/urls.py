from django.urls import path
import shopping_cart.views as cart_views


app_name = "shopping_cart"
urlpatterns = [
    path('shopping-cart/', cart_views.ShoppingCartView.as_view(),
         name="shopping-cart")
]
