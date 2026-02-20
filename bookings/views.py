from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect

from bookings.forms import BookingCreateForm
from bookings.models import Booking


def list_bookings(request: HttpRequest) -> HttpResponse:
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/list.html', context)


def create_booking(request: HttpRequest) -> HttpResponse:
    form = BookingCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {
        'form': form
    }

    return render(request, 'bookings/form.html', context)


def edit_booking(request: HttpRequest, pk: int) -> HttpResponse:
    booking = Booking.objects.get(id=pk)
    form = BookingCreateForm(request.POST or None, instance=booking)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home-page')
    context = {
        'form': form,
        'booking': booking
    }

    return render(request, 'bookings/form.html', context)


def delete_booking(request: HttpRequest, pk: int) -> HttpResponse:
    ...