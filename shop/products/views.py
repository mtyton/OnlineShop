from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage
from products.models import Product, Category, Size
from shopping_cart.models import Order
from products.forms import AddProductForm, ProductFilterForm


class BaseSupervisorControlledView(object):
    def is_supervisor(self, user):
        """
        Simply gives True if user is supervisor and returns False if user is
        not a supervisor
        Supervisor - user who can perform some super actions (for more info see the docs)
        """
        if user.is_authenticated:
            return user.is_staff or user.group.name=="salesman"
        else:
            return False


class ProductListView(View, BaseSupervisorControlledView):
    """
    use this to generate list of products on your website
    """
    model = Product
    template_name = 'products/product_list.html'
    paginator_class = Paginator

    def get(self, request, category_type, page):
        request_data = request.GET or None
        queryset = self.get_queryset(category_type, request_data)

        # paginating queryset
        paginator = self.paginator_class(queryset['products'], 6)
        try:
            queryset['products'] = paginator.page(page)
        except EmptyPage:
            # if there is nothing on this page redirect to first page
            queryset['products'] = paginator.page(1)
            return redirect(reverse(
                'products:products',
                kwargs={'category_type': category_type, 'page': 1}))

        context = {'is_supervisor': self.is_supervisor(request.user)}
        context.update(queryset)
        context['filter_form'] = ProductFilterForm(category_type=category_type)
        context['page'] = page
        context['category_type'] = category_type
        if request_data:
            context['filter_form'] = ProductFilterForm(
                request_data, category_type=category_type)

        return render(request, self.template_name, context=context)

    def get_queryset(self, category_type, request_data=None):
        prod_list = []
        temp_dict = {}
        product_queryset = Product.objects.filter(
            product_category__category_type=category_type
        )
        # filtering of products for future
        if request_data:
            product_queryset = self.filter_queryset(product_queryset,
                                                    request_data)

        for product in product_queryset:
            temp_dict['product'] = product
            temp_dict['main_image'] = product.productimage_set.get(
                is_main_image=True)
            prod_list.append(temp_dict)
            temp_dict = {}
        return {'products': prod_list}

    def filter_queryset(self, product_queryset, data):
        # first check price
        product_queryset = product_queryset.filter(
            price__range=[data.get('min_price'), data.get('max_price')]
        )

        if data.get('category'):
            # problem while using querydict, just make this normal dict
            data = dict(data)
            product_queryset = product_queryset.filter(
                product_category__in=data['category'])
        return product_queryset


class ProdctDetailView(View, BaseSupervisorControlledView):
    model = Product
    template_name = 'products/product_detail.html'
    supervisor_groups = ['admins', 'salesman']

    def get(self, request, pk):
        product = Product.objects.get(id=int(pk))
        context = {
            'product': product,
            'is_supervisor': self.is_supervisor(request.user),
            'product_form': AddProductForm(
                **{'size_set': product.get_all_available_sizes()}),
            'prod_images': product.productimage_set.all()
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        order = Order.objects.get_current_user_order(user=request.user)
        size = Size.objects.get(id=request.POST['size'])
        product = Product.objects.get(id=pk)
        quantity = request.POST['quantity']
        kwargs = {
            'order': order,
            'size': size,
            'product': product,
            'quantity': quantity
        }
        Order.objects.add_product_to_order(**kwargs)
        return redirect(reverse('shopping_cart:shopping-cart'))



