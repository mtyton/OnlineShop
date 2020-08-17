from django.contrib import admin
from web_shop.models import (Product, ProductImage, Category,
                             ProductRating, ContactData, Customer,
                             Order, ProductOrder)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductRating)
admin.site.register(ContactData)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ProductOrder)
