from django.db import models


class CarouselData(models.Model):
    upload_date = models.DateTimeField(auto_now=True, blank=False)
    image = models.ImageField(upload_to='carousel')

    @classmethod
    def get_latest_images(cls):
        return cls.objects.order_by('-upload_date')[:3]