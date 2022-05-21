from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from products import models as products_models
from rest_framework.viewsets import ReadOnlyModelViewSet
from shop_api.serializers import products as products_serializers


class CategoryModelViewSet(ReadOnlyModelViewSet):
    serializer_class = products_serializers.CategoryReadSerializer
    model = products_models.Category

    def get_queryset(self) -> QuerySet:
        """
        This returns always categories for given parent_category, if
        parent_category is not given it returns top-level categories.
        """
        if parent_category := self.request.GET.get("parent_category"):
            category = get_object_or_404(self.model, pk=parent_category)
            return category.sub_categories

        return self.model.objects.filter(parent_category=None)


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = products_serializers.ProductReadSerializer
    model = products_models.Product

    def __filter_by_category(self, category: products_models.Category) -> QuerySet:
        bottom_level_categories = category.bottom_level_categories
        return self.model.objects.filter(product_category__in=bottom_level_categories)

    def get_queryset(self) -> QuerySet:
        category_pk = self.request.GET.get("category", -10)
        try:
            category = products_models.Category.objects.get(pk=category_pk)
        except products_models.Category.DoesNotExist:
            categories = products_models.Category.objects.all()
            queryset = self.model.objects.filter(product_category__in=categories)
        else:
            queryset = self.__filter_by_category(category)

        return queryset
