from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from web_shop.models import (Product, ProductImage, Category,
                             ProductRating, ContactData, Customer,
                             Order, ProductOrder)
from web_shop.forms import RegisterForm


class RegisterView(View):
    template = "registration/register.html"

    def get(self, request):
        context = {'form': RegisterForm()}
        return render(request, self.template, context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = self.save_form_data(form.cleaned_data)
            login(request, user=customer.user)
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, self.template, context)

    def save_form_data(self, form_data):
        user = User.objects.create(username=form_data.get('username'),
                                  password=form_data.get('password'),
                                  email=form_data.get('email'))
        contact_data = ContactData.objects.create(
            first_name=form_data.get('first_name'),
            surname=form_data.get('surname'),
            country=form_data.get('country'),
            city=form_data.get('city'),
            street=form_data.get('street'),
            zip_code=form_data.get('zip_code'),
            building_number=form_data.get('building_number'),
            flat_number=form_data.get('flat_number'),
            email=form_data.get('email'),
            phone=form_data.get('phone')
        )
        customer = Customer.objects.create(user=user, contact_data=contact_data)
        return customer


class HomeView(View):
    def get(self, request):
        return render(request, 'web_shop/index.html')

    def post(self, request):
        pass


class ProductListView(View):
    """
    use this to generate list of products on your website
    """
    model = Product
    template_name = 'web_shop/product_list.html'

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
    template_name = 'web_shop/product_detail.html'

    def get(self, request, pk):
        context = {}
        context['product'] = Product.objects.get(id=int(pk))
        return render(request, self.template_name, context)


class ContactView(View):
    template_name = 'web_shop/contact.html'

    def get(self, request):
        contact_data = {
            'phone': "",
            'email': "",
            'bank_account': ""
        }
        return render(request, self.template_name, context=contact_data)


class ProfileView(View):
    template_name = 'web_shop/profile.html'

    def get(self, request):
        context = {'form': ""}
        return render(request, self.template_name)

    def post(self, request):
        pass
