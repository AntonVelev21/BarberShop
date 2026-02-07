from http.client import HTTPResponse
from django.http.request import HttpRequest


def list_barbers(request: HttpRequest) -> HTTPResponse:
    ...


def barber_details(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def add_barber(request: HttpRequest) -> HTTPResponse:
    ...


def edit_barber(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def delete_barber(request: HttpRequest, slug: str) -> HTTPResponse:
    ...