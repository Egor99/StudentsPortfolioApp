from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=256)
    results = models.CharField(max_length=512)
    rating = models.FloatField()
    university = models.CharField(max_length=128)
    speciality = models.CharField(max_length=256)
    graduate = models.BooleanField(default=False)


    def __str__(self):
        return self.name