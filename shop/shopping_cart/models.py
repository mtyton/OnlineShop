from django.db import models
from products.models import Product, Size
from customer_profile.models import Customer


class OrderManager(models.Manager):
    """
    This class suppose to manage orders
    """
    def get_current_user_order(self, user):
        try:
            customer = Customer.objects.get(user=user)
        except models.ObjectDoesNotExist:
            return None
        else:
            return self.get_or_create(customer=customer, ordered=False)[0]

    def add_product_to_order(self, *args, **kwargs):
        """
        This method does all necessary stuff to add product to order/cart
        Thise method does not return anything.
        """
        try:
            order = ProductOrder.objects.get(
                    product=kwargs['product'], order=kwargs['order'],
                    size=kwargs['size'])
            order.quantity += int(kwargs['quantity'])
            order.save()
        except models.ObjectDoesNotExist:
            ProductOrder.objects.create(
                product=kwargs['product'], order=kwargs['order'],
                size=kwargs['size'], quantity=kwargs['quantity'])


class Order(models.Model):
    """
        If there is an existing customer in database(customer has an account),
        than contact_data is set to customer contact_data.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 null=True)
    ordered = models.BooleanField(default=False)
    ordered_at = models.DateTimeField(default=None, null=True)
    payed = models.BooleanField(default=False)
    sended = models.BooleanField(default=False)

    objects = OrderManager()

    def order(self, size):
        self.ordered = True

    def send_order_mails(self):
        pass

    def send(self):
        pass

    def __str__(self):
        return str(self.customer) + " order"


class ProductOrder(models.Model):
    """
    Product Order instance it contains info about ordered product
    """
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # TODO we need more info about product here
    # Size can be bull if product has no size
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order) + " " + str(self.product)
