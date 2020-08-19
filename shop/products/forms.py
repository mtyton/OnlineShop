from django import forms
from products.model import Product


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    max_price = forms.DecimalField(max_digits=30, decimal_places=2)
    size = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        self.fields['max_price'].default = self.get_max_product_price()

    def get_max_product_price(self):
        if not Product.objects.all():
            return 0
        return Product.objects.all().order_by('price')[-1].price
