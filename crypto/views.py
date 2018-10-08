from django.shortcuts import render, get_object_or_404
import requests
import json

from .models import CryptoNews

# Create your views here.
def home(request):

    # Grab Crypto Price Data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA&tsyms=USD,EUR")
    price_api = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price_api': price_api})


def prices(request):

    context = dict()

    if request.method == 'POST':
        q = set(['BTC','ETH','XRP','BCH','EOS','LTC','XLM','ADA','USDT','MIOTA'])
        quote = request.POST['quote'].upper()

        if quote in q:
            quote_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,EUR".format(quote))
            quote_api = json.loads(quote_request.content)
            context['quote'] = quote_api
        return render(request, 'prices.html', context)

    return render(request, 'prices.html', context)


def news_list(request):
    news = CryptoNews.objects.all()
    return render(request, 'list.html', {'news': news})


def news_detail(request, source_id):
    news = get_object_or_404(CryptoNews, source_id=source_id)
    return render(request, 'detail.html', {'news':news})
