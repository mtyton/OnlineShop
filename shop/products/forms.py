from django import forms
from products.models import Category, Product


class CategoryAddAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parent_category"].required = False
        self.fields["attributes"].required = False


class ProductFilterForm(forms.Form):
    """
    This forms is used to filter products
    """

    category = forms.MultipleChoiceField(
        required=False, widget=forms.CheckboxSelectMultiple(), choices=[], label="Kategorie"
    )
    min_price = forms.DecimalField(max_digits=30, decimal_places=2, initial=0.0, required=False)
    max_price = forms.DecimalField(max_digits=30, decimal_places=2, required=False)

    def __init__(self, *args, **kwargs):
        category_type = kwargs.pop("category_type")
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        self.fields["max_price"].initial = self.get_max_product_price()
        self.fields["max_price"].max_value = self.fields["max_price"].initial
        self.fields["category"].choices = self.get_category_choices(category_type)

    def get_max_product_price(self):
        if not Product.objects.all():
            return 0
        return Product.objects.all().order_by().latest("price").price

    def get_category_choices(self, category_type):
        choices = []
        for category in Category.objects.filter(category_type=category_type):
            choices.append((category.id, category.category_name))
        return choices


class AddProductForm(forms.Form):
    """
    This form manages adding product to cart
    """

    size = forms.ChoiceField(choices=[], label="Rozmiar: ")
    quantity = forms.IntegerField(initial=1)

    def __init__(self, *args, **kwargs):
        size_set = kwargs.pop("size_set")
        choices = self.get_size_choices(size_set)
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields["size"].choices = choices

    def get_size_choices(self, size_set):
        choices = []
        for size in size_set:
            choices.append((size.id, size.code))
        return choices
