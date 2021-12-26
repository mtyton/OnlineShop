from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Attribute(models.Model):
    attr_name = models.CharField(max_length=255)
    attr_description = models.TextField(blank=True)


class AttributeValue(models.Model):
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    # all values should be kept in CharField
    value = models.CharField(max_length=255)


class Category(models.Model):
    """
    This model keeps information about available product categories
    """
    parent_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True
    )
    category_name = models.CharField(max_length=255)
    attributes = models.ManyToManyField("Attribute")

    @property
    def sub_categories(self) -> models.QuerySet:
        return Category.objects.filter(parent_category=self)

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
    attributes_values = models.ManyToManyField("AttributeValue")

    # family hashcode gives us information to which family product belongs,
    # for example, phone X may have few memory/color versions, but all phones X
    # belongs to the X family
    # family_hashcode = models.UUIDField()
    on_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    """
    This models keeps images for products
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images")
    # is main image tells if image should be the default one
    is_main_image = models.BooleanField(default=False)
