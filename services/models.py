from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.price} euro)"



class Barber(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.URLField()
    bio = models.TextField()
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.name