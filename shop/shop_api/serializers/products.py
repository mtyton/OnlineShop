from rest_framework import serializers

from products import models as products_models


class CategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = products_models.Category
        fields = [
            'pk', 'parent_category', 'category_name',
            'attributes'
        ]


class ProductReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = products_models.Product
        fields = [
            'product_categories', 'product_name',
            'description', 'rating',
            'attributes'
        ]

    product_categories = serializers.SerializerMethodField()

    def get_product_categories(self, obj):
        return []

