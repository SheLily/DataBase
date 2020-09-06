from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
