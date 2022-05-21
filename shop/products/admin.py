from django.contrib import admin
from products.forms import CategoryAddAdminForm
from products.models import Attribute, AttributeValue, Category, Product


class CategoryAdminView(admin.ModelAdmin):
    form = CategoryAddAdminForm


admin.site.register(Category, CategoryAdminView)
admin.site.register(Product)

admin.site.register(Attribute)
admin.site.register(AttributeValue)
