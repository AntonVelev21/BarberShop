from django.forms.models import ModelForm
from django import forms
from bookings.models import Booking


class BaseBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date_and_hour': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                },
            format = '%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control bg-dark text-white border-secondary rounded-0'
            field.widget.attrs['style'] = 'padding: 12px;'


class BookingCreateForm(BaseBookingForm):
    ...


class BookingEditForm(BaseBookingForm):
    ...


class BookingDeleteForm(BaseBookingForm):
    ...