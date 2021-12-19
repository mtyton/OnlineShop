# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.db.models import ObjectDoesNotExist
# from users.forms import (RegisterForm, QuickMessageForm,
#                                     ProfileEditForm)
# from users.models import Customer, ContactData
#
#
# class RegisterView(View):
#     template = "registration/register.html"
#
#     def get(self, request):
#         context = {'form': RegisterForm()}
#         return render(request, self.template, context)
#
#     def post(self, request):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             customer = self.save_form_data(form.cleaned_data)
#             login(request, user=customer.user)
#             return redirect('home')
#         else:
#             context = {'form': form}
#             return render(request, self.template, context)
#
#     def save_form_data(self, form_data):
#         user = User.objects.create(
#             username=form_data.get('username'),
#             password=form_data.get('password'),
#             email=form_data.get('email')
#         )
#         contact_data = ContactData.objects.create(
#             first_name=form_data.get('first_name'),
#             surname=form_data.get('surname'),
#             country=form_data.get('country'),
#             city=form_data.get('city'),
#             street=form_data.get('street'),
#             zip_code=form_data.get('zip_code'),
#             building_number=form_data.get('building_number'),
#             flat_number=form_data.get('flat_number'),
#             email=form_data.get('email'),
#             phone=form_data.get('phone')
#         )
#         customer = Customer.objects.create(user=user, contact_data=contact_data)
#         return customer
#
#
# class ContactView(View):
#     template_name = 'users/contact.html'
#
#     def get(self, request):
#         contact_data = {
#             'phone': "",
#             'email': "",
#             'bank_account': ""
#         }
#         form = QuickMessageForm()
#         context = {
#             'contact_data': contact_data,
#             'form': form
#         }
#         return render(request, self.template_name, context=context)
#
#
# class ProfileView(View):
#     template_name = 'users/profile.html'
#
#     def get(self, request):
#         try:
#             contact_data = Customer.objects.get(user=request.user)
#         except ObjectDoesNotExist:
#             contact_data = ContactData.objects.create()
#             Customer.objects.create(user=request.user,
#                                     contact_data=contact_data)
#         context = {'form': ProfileEditForm(instance=contact_data)}
#         return render(request, self.template_name, context=context)
#
#     def post(self, request):
#         pass
#
#
# profile_view = login_required(ProfileView.as_view())
