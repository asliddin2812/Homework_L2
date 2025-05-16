from django.db import models
from django.utils.text import slugify


# Create your models here.

class NatoMember(models.Model):
    name = models.CharField(max_length=100, unique=True)
    joined_year = models.IntegerField()
    continent = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['joined_year']
        db_table = 'natomember'
