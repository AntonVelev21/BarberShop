from django.urls.conf import path

from bookings.views import list_bookings

app_name = 'bookings'

urlpatterns = [
    path('bookings/', list_bookings, name='list-bookings')
]