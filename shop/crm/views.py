# rom django.http import Http404
# rom django.shortcuts import render, redirect, reverse
# rom django.contrib.admin.views.decorators import staff_member_required
# rom django.views import View
# rom django.views.generic import ListView, DetailView
# rom crm.forms import (BaseProductInfoForm, ProductAvailabilityForm,
#                       ProductImageForm, AvailabilityUpdateForm, AddImageForm)
# rom products.models import Category, Size, ProductAvailability, Product
# rom crm.utils import FormDataExtractor
# rom shopping_cart.models import Order, ProductOrder


# lass AddProductView(View):
#    data_extractor = FormDataExtractor()
#    step_validity = False

#    def get(self, request, step_numb=0):
#        """
#        Checks step_number, renders form for every step_number
#        """
#        forms = self.get_step_form(request, step_numb)
#        context = {'forms': forms}
#        return render(request, 'crm/product_add.html', context)

#    def post(self, request):
#        """
#        checks every step data validity and renders next step,
#        if step is a final_step this method saves data after validation once
#        more
#        """
#        step_numb = self.retrieve_step_number(request)
#        # step with number 2 is the final one

#        if step_numb == 2:
#            # validate image form here to make i easier
#            image_form = ProductImageForm(request.POST, request.FILES)
#            if image_form.is_valid():
#                self.save(image_form)
#                # TODO fix category type
#                return redirect(reverse('products:products',
#                                        kwargs={'category_type': "cloth",
#                                                'page': 1}))
#            else:
#                return self.render_invalid_form(request, [image_form])

#        forms = self.form_storage_picker(step_numb, request.POST)
#        if not self.step_validity:
#            return self.render_invalid_form(request, forms)
#        # if step is valid change it back to false
#        self.step_validity = False

#        step_numb += 1
#        return self.get(request, step_numb)

#    def render_invalid_form(self, request, forms):
#        """
#        render forms with errors
#        """
#        context = {'forms': forms}
#        return render(request, 'crm/product_add.html', context)

#    def retrieve_step_number(self, request):
#        """
#        retrieves step_number from post
#        """
#        try:
#            step_numb = int(request.POST.get('step_numb'))
#        except:
#            step_numb = int(request.POST.get('step_numb')[0])
#        return step_numb

#    def get_step_form(self, request, step_numb):
#        if step_numb == 0:
#            func = self.get_first_step_forms
#        elif step_numb == 1:
#            func = self.get_second_step_forms
#        elif step_numb == 2:
#            func = self.get_third_step_forms
#        else:
#            func = self.get_none_form
#        return func(request)

#    def get_first_step_forms(self, request):
#        return [BaseProductInfoForm()]

#    def get_second_step_forms(self, request):
#        category_id = int(request.POST.get('product_category', None))
#        category = Category.objects.get(id=category_id)
#        forms = []
#        for size in category.size_set.all():
#            forms.append(ProductAvailabilityForm(**{"pre_submit_size": size}))
#        return forms

#    def get_third_step_forms(self, request):
#        return[ProductImageForm()]

#    def get_none_form(self, request):
#        return None

#    def form_storage_picker(self, step_number, data):
#        if step_number == 0:
#            forms = self.store_first_step_form(data, BaseProductInfoForm)
#        elif step_number == 1:
#            data = dict(data)
#            forms = self.store_second_step_forms(data, ProductAvailabilityForm)
#        else:
#            forms = []
#        return forms

#    def store_first_step_form(self, data, form_class):
#        """
#        Saves in session first step form data
#        :param request:
#        :return:
#        """
#        form = form_class(data)
#        if form.is_valid():
#            self.step_validity = True
#            self.save_forms_data_to_session(form.data, form_class.get_name())
#        return [form]

#    def store_second_step_forms(self, data, form_class):
#        """
#        Saves in session second step forms data (there are multiple forms)
#        :param request:
#        :return:
#        """
#        data = self.data_extractor.create_data_packages(data, len(data['size']))
#        forms = []
#        self.step_validity = True
#        for d in data:
#            form = form_class(d)
#            forms.append(form)
#            if not form.is_valid():
#                self.step_validity = False
#        if self.step_validity:
#            for number, form in enumerate(forms):
#                form_name = form_class.get_name() + '_' + str(number)
#                self.save_forms_data_to_session(form.data, form_name)
#        return forms

#    def save_forms_data_to_session(self, form_data, form_name):
#        self.request.session[form_name] = form_data

#    def save(self, valid_image_form):
#        # base info form
#        base_info_data = self.request.session.pop("BaseProductInfoForm")
#        base_info_form = BaseProductInfoForm(base_info_data)
#        if base_info_form.is_valid():
#            product = base_info_form.save()
#        else:
#            return Http404("wrong")

#        # availability form
#        for key, value in self.request.session.items():
#            if "ProductAvailabilityForm" in key:
#                availability_form = ProductAvailabilityForm(value)
#                if availability_form.is_valid():
#                    availability_form.save(**{'product_id': product.id})

#        # Image Form
#        valid_image_form.save(**{'product_id': product.id})


# dd_product_view = staff_member_required(AddProductView.as_view())


# lass AvailabilityUpdateView(View):

#    def get(self, request, product_id):
#        product = Product.objects.get(id=product_id)
#        forms = []
#        for availability in ProductAvailability.objects.filter(product=product):
#            forms.append(AvailabilityUpdateForm(instance=availability))
#        return render(
#            request, 'crm/availability_edit_form.html', context={'forms': forms}
#        )

#    def post(self, request, product_id):
#        post = dict(request.POST)
#        index = 0
#        product = Product.objects.get(id=product_id)
#        for availability in ProductAvailability.objects.filter(product=product):
#            data = {
#                'size': post.get('size')[index],
#                'quantity': int(post.get('quantity')[index])
#            }
#            form = AvailabilityUpdateForm(data, instance=availability)
#            if form.is_valid():
#                form.save()
#            index += 1
#        category_type = product.product_category.category_type
#        return redirect(reverse('products:product',
#                                kwargs={'category_type': category_type,
#                                        'page': 1}))


# pdate_availability_view = staff_member_required(
#    AvailabilityUpdateView.as_view())


# lass UploadImageForm(View):

#    def get(self, request, product_id):
#        context = {
#            'form': AddImageForm(),
#        }
#        return render(request, 'crm/upload_image_form.html', context)

#    def post(self, request, product_id):
#        product = Product.objects.get(id=product_id)
#        form = AddImageForm(request.POST)
#        import ipdb
#        ipdb.set_trace()
#        if form.is_valid():
#            form.save(**{'product': product})
#            category_type = product.product_category.category_type
#            return redirect(reverse('products:product',
#                                    kwargs={'category_type': category_type,
#                                            'page': 1}))
#        else:
#            return self.get(request, product_id)


# mage_upload_view = staff_member_required(UploadImageForm.as_view())


# lass OrderListView(ListView):
#    model = Order
#    template_name = ""

#    def get_queryset(self):
#        return self.model.objects.all()


# lass OrderDetailView(DetailView):
#    model = Order

#    def get_queryset(self):
#        pass

#    def get_context_data(self, **kwargs):
#        pass
