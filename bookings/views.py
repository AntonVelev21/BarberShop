from http.client import HTTPResponse

from django.http.request import HttpRequest


def list_bookings(request: HttpRequest) -> HTTPResponse:
    ...


def booking_details(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def create_booking(request: HttpRequest) -> HTTPResponse:
    ...


def edit_booking(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def delete_booking(request: HttpRequest, pk: int) -> HTTPResponse:
    ...