from django.db import models


class Promotions(models.Model):
    upload_date = models.DateTimeField(auto_now=True, blank=False)
    promotion_title = models.CharField(max_length=255)

    image = models.ImageField(upload_to='carousel')
    promotion_url = models.URLField()

    @classmethod
    def get_latest(cls) -> models.QuerySet:
        """
        Returns 3 latest promotions
        """
        return cls.objects.order_by('-upload_date')[:3]
