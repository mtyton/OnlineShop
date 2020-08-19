from django.db import models
from products.models import Product
from customer_profile.models import Customer


class Order(models.Model):
    """
        If there is an existing customer in database(customer has an account),
        than contact_data is set to customer contact_data.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 null=True)
    ordered = models.BooleanField(default=False)

    def order(self):
        self.ordered = True


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    pass