from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ContactData(models.Model):
    """
        Contact data for user/order.
        Contact data is used to send messages/deliver
    """
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=12)
    building_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=9)


class Customer(models.Model):
    """
        Customer's profile model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE)