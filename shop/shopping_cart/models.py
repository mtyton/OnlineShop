from django.db import models

from users.models import PersonCustomer


class OrderManager(models.Manager):
    pass


class Order(models.Model):
    """
    If there is an existing customer in database(customer has an account),
    then contact_data is set to customer contact_data.
    """
    registered_customer = models.ForeignKey(
        "users.PersonCustomer", on_delete=models.CASCADE, null=True
    )
    anonymous_customer = models.ForeignKey(
        "users.AnonymousCustomer",
        on_delete=models.CASCADE, null=True
    )

    ordered = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(default=None, null=True)

    # TODO - add payment integration
    # payment_method = models.CharField(max_length=255)
    payed = models.BooleanField(default=False)
    user_notified = models.BooleanField(default=False)

    objects = OrderManager()

    def order(self, size):
        self.ordered = True

    def notify_user(self):
        pass

    def send(self):
        pass

    def __str__(self):
        return str(self.customer) + " order"


class ProductOrder(models.Model):
    """
    Product Order instance it contains info about ordered product
    """
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order) + " " + str(self.product)
