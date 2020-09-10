from django.contrib import admin
from products.models import (Product, Category, Size, ProductAvailability,
                             ProductImage, ProductRating)


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(ProductAvailability)
admin.site.register(ProductImage)
admin.site.register(ProductRating)
