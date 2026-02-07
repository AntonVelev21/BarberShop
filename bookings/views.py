from http.client import HTTPResponse

from django.http.request import HttpRequest


def list_reservations(request: HttpRequest) -> HTTPResponse:
    ...


def reservation_details(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def make_reservation(request: HttpRequest) -> HTTPResponse:
    ...


def edit_reservation(request: HttpRequest, pk: int) -> HTTPResponse:
    ...


def delete_reservation(request: HttpRequest, pk: int) -> HTTPResponse:
    ...