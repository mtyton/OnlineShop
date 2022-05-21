from django.contrib.auth.models import User
from django.test import TestCase


class ExtendedTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.admin = self._create_admin_user()
        self.user = self._create_user()

    def _create_user(self, username="testUser", password="complexPassword") -> User:
        return User.objects.create_user(username=username, password=password)

    def _create_admin_user(self, username="testAdmin", password="complexPassword") -> User:
        return User.objects.create_superuser(username=username, password=password)
