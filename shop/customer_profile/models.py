from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BaseContactModel(models.Model):
    """
        Contact data for user/order.
        Contact data is used to send messages/deliver
    """
    class Meta:
        abstract = True

    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=12)
    building_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.first_name + " " + self.surname


class PersonCustomer(BaseContactModel):
    """
        Customer's profile model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
