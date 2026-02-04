from django.db import models
from django.db.models.deletion import SET_NULL


class Reservation(models.Model):
    client_name = models.CharField(max_length=50)
    client_phone = models.CharField(max_length=20)
    date_and_hour = models.DateTimeField()
    barber = models.ForeignKey('services.Barber', on_delete=SET_NULL, null=True, blank=True)
    services = models.ManyToManyField('services.Service', related_name='reservations')

    @property
    def total_price(self):
        total = self.services.aggregate(total=models.Sum('price'))['total'] or 0.00
        return f"Reservation for {total} on {self.date_and_hour}"

    def __str__(self):
        return f"Booking for {self.client_name} on {self.date_and_hour}"
