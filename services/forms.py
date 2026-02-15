from django.forms.models import ModelForm
from services.models import Barber, Service


class BaseBarberForm(ModelForm):
    class Meta:
        model = Barber
        exclude = ['slug']


class BarberCreateForm(BaseBarberForm):
    ...


class BarberEditForm(BaseBarberForm):
    ...


class BarberDeleteForm(BaseBarberForm):
    ...


class BaseServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['slug']


class ServiceCreateForm(BaseServiceForm):
    ...


class ServiceEditForm(BaseServiceForm):
    ...


class ServiceDeleteForm(BaseServiceForm):
    ...