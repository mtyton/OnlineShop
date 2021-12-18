from django.shortcuts import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from commons.tests import ExtendedTestCase
from web_shop.models import Promotion


class HomeViewTestCase(ExtendedTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('home')

    def test_get_no_promotions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='web_shop/index.html'
        )

    def test_get_success_no_auth(self):
        for i in range(3):
            Promotion.objects.create(
                promotion_title=f"testPromotion{i}",
                image=SimpleUploadedFile(
                    name=f"image{i}.jpg",
                    content="", content_type="image/jpeg"
                )
            )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='web_shop/index.html'
        )

    def test_get_success_user_authenticated(self):
        for i in range(3):
            Promotion.objects.create(
                promotion_title=f"testPromotion{i}",
                image=SimpleUploadedFile(
                    name=f"image{i}.jpg",
                    content="", content_type="image/jpeg"
                )
            )

        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='web_shop/index.html'
        )
