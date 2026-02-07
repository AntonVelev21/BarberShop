from django.db import models
from django.template.defaultfilters import slugify


class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.price} euro)"



class Barber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    image_url = models.URLField()
    bio = models.TextField()
    years_of_experience = models.IntegerField()
    slug = models.CharField(max_length=50, unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name}-{self.last_name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'