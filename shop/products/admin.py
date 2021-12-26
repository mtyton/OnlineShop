from django.contrib import admin

from products.models import Product, Category
from products.forms import CategoryAddAdminForm


class CategoryAdminView(admin.ModelAdmin):
    form = CategoryAddAdminForm


admin.site.register(Category, CategoryAdminView)
admin.site.register(Product)
