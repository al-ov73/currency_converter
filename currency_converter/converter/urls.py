from django.urls import path

from currency_converter.converter.views import exchange

urlpatterns = [
    path('', exchange, name='exchange')
]