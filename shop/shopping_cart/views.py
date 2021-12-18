# from django.shortcuts import render, reverse, redirect
# from django.views import View
# from django.contrib.auth.decorators import login_required
# from django.db.models import ObjectDoesNotExist
# from shopping_cart.models import Order, ProductOrder
# from customer_profile.models import Customer
# from products.models import Product
#
#
# class ShoppingCartView(View):
#     template_name = "shopping_cart/shopping_cart.html"
#
#     def get(self, request):
#         if not request.user.is_authenticated:
#             return redirect(reverse('customer_profile:login'))
#         order = Order.objects.get_current_user_order(user=request.user)
#         context = {
#             'order': order,
#             'ordered_products': order.productorder_set.all()
#         }
#         return render(request, 'shopping_cart/shopping_cart.html', context)
#
#     def post(self, request, product_id):
#         pass
#
#     def add_product_to_order(self, order, product_id):
#         product = Product.objects.get(id=product_id)
#         ProductOrder.objects.create(order=order, product=product)
#
#
# shopping_cart_view = login_required(ShoppingCartView.as_view())