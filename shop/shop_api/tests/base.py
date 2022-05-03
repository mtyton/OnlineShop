from rest_framework.test import APIClient

from common.tests import ExtendedTestCase


class ExtendedShopApiTestCase(ExtendedTestCase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

