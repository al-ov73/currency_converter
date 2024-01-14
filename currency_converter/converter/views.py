import requests
from django.shortcuts import render

from currency_converter import settings
from currency_converter.converter.forms import CurrencyConverter


def exchange(request):

    if request.method == 'GET':
        form = CurrencyConverter()
        return render(request=request, template_name='converter/index.html', context={
            'form': form,
        })

    if request.method == 'POST':

        form = CurrencyConverter(request.POST)
        from_cur = request.POST.get('from_cur')
        to_cur = request.POST.get('to_cur')
        amount = request.POST.get('amount')
        response = requests.get(url=f'https://v6.exchangerate-api.com/v6/{settings.API_ID}/pair/{from_cur}/{to_cur}/{amount}').json()
        result = response.get('conversion_result')
        return render(request=request,
                      template_name='converter/index.html',
                      context={
                          'form': form,
                          'result': result,
                          'from_cur': from_cur,
                          'to_cur': to_cur,
                          'amount': amount,
                      })