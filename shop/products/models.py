from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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


class Product(models.Model):
    """
        Simply products available on store
    """
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(max_length=2500)
    added_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    @property
    def rate(self):
        rating = ProductRating.objects.get(product=self).rating
        return rating


    def is_available(self):
        return True

    def __str__(self):
        return self.product_name


class Size(models.Model):
    code = models.CharField(max_length=100)


class ProductAvalability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name="number_per_size")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


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
