from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseDeliveryModel(models.Model):
    """
    Contact data for user/order.
    Contact data is used to send messages/deliver
    """

    class Meta:
        abstract = True

    country = models.ForeignKey("regions.Country", on_delete=models.CASCADE)

    # address
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=12)
    building_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.first_name + " " + self.surname


class BaseContactModel(BaseDeliveryModel):
    class Meta:
        abstract = True

    # contact data
    # if user already have an account he may want to use different email for delivery
    email = models.EmailField()
    phone = models.CharField(max_length=25, null=True)


class PersonCustomer(BaseContactModel):
    """
    Customer's profile model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class AnonymousCustomer(BaseContactModel):
    date_created = models.DateField(auto_now_add=True)
