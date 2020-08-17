from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Category(models.Model):
    """
        This model suppose to store all available product categories.
    """
    AVAILABLE_CATEGORY_TYPES = [('cloth', 'cloth'), ('other', 'other')]

    category_type = models.CharField(
        choices=AVAILABLE_CATEGORY_TYPES, max_length=50)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    """
        Simply products available on store
    """
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(max_length=2500)
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = ProductManager

    @property
    def rate(self):
        rating = ProductRating.objects.get(product=self).rating
        return rating

    @staticmethod
    def is_available():
        return True

    def __str__(self):
        return self.product_name


class ProductAvalability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="number_per_size")
    size = models.CharField(max_length=250)
    number = models.IntegerField(default=0)


class ProductImage(models.Model):
    """
        This model stores product images, every product can have many images.
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.image.url


class ProductRating(models.Model):
    """
        Every product should have it's own rate.
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )


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


class Order(models.Model):
    """
        If there is an existing customer in database(customer has an account),
        than contact_data is set to customer contact_data.

    """
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE,
                                 null=True)
    contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE)


class ProductOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)


class SellStats(models.Model):
    pass