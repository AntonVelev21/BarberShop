from http.client import HTTPResponse

from django.http.request import HttpRequest
from django.shortcuts import render


def list_bookings(request: HttpRequest) -> HTTPResponse:
    return render(request, 'bookings/list.html')


def booking_details(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def create_booking(request: HttpRequest) -> HTTPResponse:
    ...


def edit_booking(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def delete_booking(request: HttpRequest, pk: int) -> HTTPResponse:
    ...