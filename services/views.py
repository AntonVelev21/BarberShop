from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404

from services.models import Barber, Service


def list_barbers(request: HttpRequest) -> HttpResponse:
    barbers = Barber.objects.all()
    context = {
        'barbers': barbers
    }
    return render(request, 'barbers/list.html', context)


def barber_details(request: HttpRequest, slug: str) -> HttpResponse:
    barber = get_object_or_404(Barber, slug=slug)
    context = {
        'barber': barber
    }
    return render(request, 'barbers/details.html', context)


def create_barber(request: HttpRequest) -> HttpResponse:
    ...


def edit_barber(request: HttpRequest, slug: str) -> HttpResponse:
    ...


def delete_barber(request: HttpRequest, slug: str) -> HttpResponse:
    ...


def list_services(request: HttpRequest) -> HttpResponse:
    services = Service.objects.all()
    context = {
        'services': services
    }

    return render(request, 'services/list.html', context)


def service_details(request: HttpRequest, slug: str) -> HttpResponse:
    service = get_object_or_404(Service, slug=slug)
    context = {
        'service': service
    }
    return render(request, 'services/details.html', context)


def create_service(request: HttpRequest) -> HttpResponse:
    ...


def edit_service(request: HttpRequest, slug: str) -> HttpResponse:
    ...


def delete_service(request: HttpRequest, slug: str) -> HttpResponse:
    ...