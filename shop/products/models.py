from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


SIZE_TYPES = [
    ('standard', 'standard')
]


class Category(models.Model):
    """
        This model keeps information about available product categories
    """

    category_name = models.CharField(max_length=255)

    parent_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True
    )

    @property
    def sub_categories(self) -> models.QuerySet:
        return Category.objects.get(parent_category=self)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
        This models keeps data about particular product
    """
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField(max_length=2500)
    price = models.DecimalField(max_digits=30, decimal_places=2)

    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )

    @property
    def available_products(self):
        return ProductAvailability.objects.filter(product=self)

    def get_all_available_sizes(self):
        return Size.objects.filter(category=self.product_category)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    """
        This model stores product images, every product can have many images.
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")
    is_main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.image.url


class Size(models.Model):
    code = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class ProductAvailability(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, verbose_name="Product"
    )
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
