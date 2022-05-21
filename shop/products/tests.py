from common.tests import ExtendedTestCase
from products.models import Category


class CategoryModelTestCase(ExtendedTestCase):
    fixtures = ["test_full_products.json"]

    def test_bottom_level_categories_success(self):
        top_level_category = Category.objects.filter(parent_category=None).first()
        bottom_level_categories = top_level_category.bottom_level_categories
        for category in bottom_level_categories:
            self.assertEqual(category.sub_categories.count(), 0)

    def test_bottom_level_categories_for_bottom_level_category(self):
        # first create some bottom level category
        category = Category.objects.create(category_name="LonelyCategory")
        self.assertEqual(category.sub_categories.count(), 0)
        self.assertEqual(category.bottom_level_categories.count(), 1)
        self.assertEqual(category.bottom_level_categories.first().pk, category.pk)

    def test_bottom_level_category_multiple_categories(self):
        expected_categories = []
        top_level_category = Category.objects.filter(parent_category=None).first()
        mid_level_category = top_level_category.sub_categories.first()
        # create multiple bottom level categories for mid level category
        for i in range(5):
            expected_categories.append(
                Category.objects.create(category_name=f"LonelyCategory{i}", parent_category=mid_level_category)
            )
        bottom_level_categories = top_level_category.bottom_level_categories
        self.assertEqual(bottom_level_categories.count(), len(expected_categories))
        for category in expected_categories:
            self.assertTrue(bottom_level_categories.filter(pk=category.pk).exists())
