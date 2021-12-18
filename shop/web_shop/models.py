from django.db import models


class PromotionManager(models.Manager):

    def get_latest_promotions(self, count=3) -> models.QuerySet:
        """
        Returns 3 latest promotions
        """
        items = self.exclude(image=None).order_by('-upload_date')
        if items.count() >= count:
            return items

        return items[:count]


class Promotion(models.Model):
    upload_date = models.DateTimeField(auto_now=True, blank=False)
    promotion_title = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to='carousel', null=True
    )
    promotion_url = models.URLField()

    objects = PromotionManager()
