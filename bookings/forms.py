from django.core.exceptions import ValidationError
from django.forms.models import ModelForm
from bookings.models import Booking


class BaseBookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control bg-dark text-white border-secondary rounded-0'
            field.widget.attrs['style'] = 'padding: 12px;'
            if field_name == 'date_and_hour':
                field.widget.input_type = 'datetime-local'

    def clean_client_name(self):
        entered_name = self.cleaned_data.get('client_name')
        if ' ' not in entered_name:
            raise ValidationError('Please enter second name!')
        return entered_name


class BookingCreateForm(BaseBookingForm):
    ...


class BookingEditForm(BaseBookingForm):
    ...


class BookingDeleteForm(BaseBookingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True