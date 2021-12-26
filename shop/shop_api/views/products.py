from rest_framework.viewsets import ReadOnlyModelViewSet
from django.shortcuts import get_object_or_404

from shop_api.serializers import products as products_serializers
from products import models as products_models


class CategoryModelViewSet(ReadOnlyModelViewSet):
    serializer_class = products_serializers.CategoryReadSerializer
    model = products_models.Category

    def get_queryset(self):
        """
        This returns always categories for given parent_category, if
        parent_category is not given it returns top-level categories.
        """
        if parent_category := self.request.GET.get('parent_category'):
            category = get_object_or_404(self.model, pk=parent_category)
            return category.sub_categories

        return self.model.objects.filter(parent_category=None)


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = products_serializers.ProductReadSerializer
    model = products_models.Product

    def get_queryset(self):
        pass

