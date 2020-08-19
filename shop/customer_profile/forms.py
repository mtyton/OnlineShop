from customer_profile.models import Customer
from django import forms


ACCESSIBLE_COUNTRIES = [("Poland", "Poland")]


class ContactForm(forms.Form):
    # contact data part
    first_name = forms.CharField(label="First Name: ", max_length=255)
    surname = forms.CharField(label="Surname: ", max_length=255)
    country = forms.ChoiceField(label="Country: ",
                                choices=ACCESSIBLE_COUNTRIES)
    city = forms.CharField(label="City: ", max_length=255)
    street = forms.CharField(label="Street and flat: ", max_length=255)
    zip_code = forms.CharField(label="Zip Code: ", max_length=25)
    building_number = forms.CharField(label="Building Number: ", max_length=50)
    flat_number = forms.CharField(label="Flat Number: ", max_length=50)
    phone = forms.CharField(max_length=50)


class RegisterForm(ContactForm):
    # users part
    username = forms.CharField(label="Username: ", max_length=255)
    password = forms.CharField(label="Password: ", max_length=255,
                               widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Repeat Password: ", max_length=255,
                                      widget=forms.PasswordInput)
    email = forms.EmailField(label="E-mail")