from django.db import models

class  DigitalCurrency(models.Model):
    ticker = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=15, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ticker']

