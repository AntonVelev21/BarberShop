from http.client import HTTPResponse
from django.http.request import HttpRequest


def list_barbers(request: HttpRequest) -> HTTPResponse:
    ...


def barber_details(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def create_barber(request: HttpRequest) -> HTTPResponse:
    ...


def edit_barber(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def delete_barber(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def list_services(request: HttpRequest) -> HTTPResponse:
    ...


def service_details(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def create_service(request: HttpRequest) -> HTTPResponse:
    ...


def edit_service(request: HttpRequest, slug: str) -> HTTPResponse:
    ...


def delete_service(request: HttpRequest, slug: str) -> HTTPResponse:
    ...