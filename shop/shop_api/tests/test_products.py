from django.shortcuts import reverse
from products import models as product_models

from shop.shop_api.test_mixins.base import ExtendedShopApiTestCase


class CategoryModelViewSetTestCase(ExtendedShopApiTestCase):
    def __create_category(self, parent_category=None):
        category_name = "TopLevel" if not parent_category else "SubCategory"
        return product_models.Category.objects.create(parent_category=parent_category, category_name=category_name)

    def setUp(self):
        super().setUp()
        self.url = reverse("category-list")
        self.parent_category = self.__create_category()
        self.child_category = self.__create_category(self.parent_category)
        self.grandson_category = self.__create_category(self.child_category)

    def test_get_categories_success_no_params(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["pk"], self.parent_category.pk)

    def test_get_categories_success_bottom_category(self):
        response = self.client.get(self.url, data={"parent_category": self.child_category.pk})
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0]["pk"], self.grandson_category.pk)

    def test_get_category_wrong_pk(self):
        response = self.client.get(self.url, data={"parent_category": -231})
        self.assertEqual(response.status_code, 404)


class ProductViewSetTestCase(ExtendedShopApiTestCase):
    fixtures = ["test_full_products.json"]

    def setUp(self):
        super().setUp()
        self.url = reverse("product-list")

    def test_get_queryset_no_category(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        # TODO this should return top rated products in near future
        content = response.json()
        self.assertNotEqual(len(content), 0)

    def test_get_queryset_top_level_category(self):
        top_level_category = product_models.Category.objects.filter(parent_category=None).first()

        response = self.client.get(self.url, data={"category": top_level_category.pk})
        self.assertEqual(response.status_code, 200)
        # TODO this should return most popular products in near future
        content = response.json()
        self.assertNotEqual(len(content), 0)

    def test_get_queryset_bottom_level_category(self):
        category = product_models.Category.objects.filter(parent_category=None).first()
        while category.sub_categories.count() != 0:
            category = category.sub_categories.first()

        response = self.client.get(self.url, data={"category": category.pk})
        self.assertEqual(response.status_code, 200)
        # TODO this should return most popular products in near future
        content = response.json()
        self.assertNotEqual(len(content), 0)
        for elem in content:
            self.assertEqual(elem["product_category"], category.pk)
