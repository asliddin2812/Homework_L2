from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
def validate_joined_year(value):
    if value.year > timezone.now().year:
        raise ValidationError("To'gri yilni kiriting janob!")

class NatoMember(models.Model):
    name = models.CharField(max_length=100, unique=True)
    joined_year = models.DateTimeField(auto_now_add=True)
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
