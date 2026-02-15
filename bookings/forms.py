from django.forms.models import ModelForm

from bookings.models import Booking


class BaseBookingForm(ModelForm):
    class Meta:
        model = Booking


class BookingCreateForm(BaseBookingForm):
    ...


class BookingEditForm(BaseBookingForm):
    ...


class BookingDeleteForm(BaseBookingForm):
    ...