from django import forms
import requests

from currency_converter import settings


class CurrencyConverter(forms.Form):

    response = requests.get(url=f'https://v6.exchangerate-api.com/v6/{settings.API_ID}/latest/USD').json()
    currencies = response.get('conversion_rates').keys()
    CURRENCIES = set()
    for currency in sorted(currencies):
        CURRENCIES.add((currency, currency))

    amount = forms.CharField(
        label='Enter amount',
    )
    from_cur = forms.ChoiceField(
        choices=sorted(CURRENCIES),
        label='From',
    )
    to_cur = forms.ChoiceField(
        choices=sorted(CURRENCIES),
        label='To',
    )

