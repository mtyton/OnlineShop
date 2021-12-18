from django.test import TestCase
from django.core.files import File
import mock
from web_shop.models import (Product, ProductImage, Category,
                             ProductRating, ContactData, Customer,
                             Order, ProductOrder)

# TODO - this test case should be moved elsewhere
# class TestProductModel(TestCase):
#     def setUp(self):
#         self.test_category = Category.objects.create(category_name="test_cat")
#         self.prod = Product.objects.create(
#             product_name="testname", description="desc", price=10.0,
#             on_stock=10, product_category=self.test_category,
#         )
#         self.file_mock = mock.MagicMock(spec=File)
#
#     def test_product_image_set_empty(self):
#         images = self.prod.image_set
#         self.assertEqual(len(images), 0)
#
#     def test_product_image_set(self):
#         self.file_mock.name = "test.png"
#         ProductImage.objects.create(
#             product=self.prod,
#             image=self.file_mock
#         )
#         images = self.prod.image_set
#         self.assertEqual(len(images), 1)

class HomeViewTestCase():
    pass
