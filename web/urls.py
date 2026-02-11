from django.urls.conf import path

from web.views import index, about

urlpatterns = [
    path('', index, name='home-page'),
    path('about/', about, name='about')
]