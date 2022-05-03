from django.db import models


# TODO - enabling this module should be optional
class Region(models.Model):
    slug_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Country(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
