from django.shortcuts import render
from django.views import View
from shopping_cart.models import ShoppingCart


class ShoppingCartView(View):
    template_name = "web_shop/shopping_cart.html"

    def get(self, request):
        if not request.session.get('cart'):
            request.session['cart'] = ShoppingCart()
        print(request.session.get('cart'))
        return render(request, self.template_name)

    def post(self, request):
            pass