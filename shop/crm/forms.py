from django import forms
from products.models import (Product, ProductAvailability, Size,
                             Category, ProductImage)


class BaseProductModelFormMixin(forms.ModelForm):

    step_numb = forms.IntegerField(widget=forms.HiddenInput)


class BaseProductInfoForm(BaseProductModelFormMixin):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BaseProductInfoForm, self).__init__(*args, **kwargs)
        self.fields['step_numb'].initial = 0

    @staticmethod
    def get_name():
        return "BaseProductInfoForm"


class ProductAvailabilityForm(BaseProductModelFormMixin):
    class Meta:
        model = ProductAvailability
        fields = ['size', 'quantity']

    def __init__(self, *args, **kwargs):
        size = None
        if kwargs.get('pre_submit_size'):
            size = kwargs.pop('pre_submit_size')
        super(ProductAvailabilityForm, self).__init__(*args, **kwargs)
        self.fields['step_numb'].initial = 1
        if size:
            self.fields['size'].widget.attrs['readonly'] = True
            self.fields['size'].initial = size

    @staticmethod
    def get_name():
        return "ProductAvailabilityForm"

    def save(self, commit=True, **kwargs):
        self.cleaned_data.update(kwargs)
        self.cleaned_data.pop('step_numb')
        return ProductAvailability.objects.create(**self.cleaned_data)


class ProductImageForm(BaseProductModelFormMixin):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main_image']

    def __init__(self, *args, **kwargs):
        super(ProductImageForm, self).__init__(*args, **kwargs)
        self.fields['step_numb'].initial = 2
        self.fields['is_main_image'].initial = True
        self.fields['is_main_image'].disabled = True

    @staticmethod
    def get_name():
        return "ProductImageForm"

    def save(self, commit=True, **kwargs):
        self.cleaned_data.update(kwargs)
        self.cleaned_data.pop('step_numb')
        return ProductImage.objects.create(**self.cleaned_data)


class AvailabilityUpdateForm(forms.ModelForm):

    class Meta:
        model = ProductAvailability
        fields = ['size', 'quantity']

    def __init__(self, *args, **kwargs):
        super(AvailabilityUpdateForm, self).__init__(*args, **kwargs)
        self.fields['size'].widget.attrs['readonly'] = True


class AddImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = ['image']

    def save(self, commit=True, **kwargs):
        ProductImage.objects.create(
            product=kwargs['product'], image=self.cleaned_data['image'],
            is_main_image=True
        )

