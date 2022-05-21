# from users.models import Customer
# from django import forms
#
#
# ACCESSIBLE_COUNTRIES = [("Poland", "Poland")]
#
#
# class ContactForm(forms.Form):
#     # contact data part
#     first_name = forms.CharField(label="Imię: ", max_length=255)
#     surname = forms.CharField(label="Nazwisko: ", max_length=255)
#     country = forms.ChoiceField(label="Państwo: ",
#                                 choices=ACCESSIBLE_COUNTRIES)
#     city = forms.CharField(label="Miasto: ", max_length=255)
#     street = forms.CharField(label="Ulica: ", max_length=255)
#     zip_code = forms.CharField(label="Kod pocztowy: ", max_length=25)
#     building_number = forms.CharField(label="Number budynku: ", max_length=50)
#     flat_number = forms.CharField(
#         label="Numer mieszkania: ", max_length=50, required=False)
#     phone = forms.CharField(label="Numer telefonu", max_length=50)
#
#
# class RegisterForm(ContactForm):
#     # users part
#     username = forms.CharField(label="Username: ", max_length=255)
#     password = forms.CharField(label="Password: ", max_length=255,
#                                widget=forms.PasswordInput)
#     repeat_password = forms.CharField(label="Repeat Password: ", max_length=255,
#                                       widget=forms.PasswordInput)
#     email = forms.EmailField(label="E-mail")
#
#
# class QuickMessageForm(forms.Form):
#     topic = forms.CharField()
#     response_email = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea())
#
#
# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = ContactData
#         fields = '__all__'
#
