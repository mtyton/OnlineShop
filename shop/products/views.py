from django.shortcuts import render, redirect
from django.views import View
from products.models import Product, Category


class ProductListView(View):
    """
    use this to generate list of products on your website
    """
    model = Product
    template_name = 'products/product_list.html'

    def get(self, request, prod_type):
        queryset = self.get_queryset(request, prod_type)
        context = {}
        context['queryset'] = queryset
        return render(request, self.template_name, context=context)

    def get_queryset(self, request, prod_type):
        queryset = {}
        categories = Category.objects.filter(category_type=prod_type)
        queryset['categories'] = categories.values('category_name')
        queryset['products'] = self.get_products()
        return queryset

    def get_products(self, filter_categories=()):
        prod_list = []
        temp_dict = {}
        product_queryset = Product.objects.all()
        # filtering of products for future
        if filter_categories:
            product_queryset = product_queryset.filter(
                product_category__in=filter_categories)

        for product in Product.objects.all():
            temp_dict['product'] = product
            temp_dict['prod_images'] = product.productimage_set
            temp_dict['main_image'] = product.productimage_set.get(
                is_main_image=True)
            prod_list.append(temp_dict)
            temp_dict = {}
        return prod_list


class ProdctDetailView(View):
    model = Product
    template_name = 'products/product_detail.html'

    def get(self, request, pk):
        context = {}
        context['product'] = Product.objects.get(id=int(pk))
        return render(request, self.template_name, context)
