""" File should run every 12h to get new news information """
import os
import json
import django
import requests
import sys, os, django
from textblob import TextBlob

sys.path.append("/Users/vmueller/Documents/Software Projects/testrun/mysite") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
# /Users/vmueller/Documents/Software Projects/testrun/mysite/news_automation

from crypto.models import CryptoNews

API_REQUEST = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
API = json.loads(API_REQUEST.content)

def get_news_information(api=API):
    """ Retrieves News from
    https://min-api.cryptocompare.com/
    """
    for item in api['Data']:
        if not CryptoNews.objects.filter(source_id=item['id']).exists():
            # no object satisfying query exists
            sentiment = TextBlob(item['body'])
            CryptoNews.objects.create(
                source_id=item['id'],
                body=item['body'],
                imageurl=item['imageurl'],
                source=item['source'],
                title=item['title'],
                source_url=item['url'],
                sentiment=sentiment.sentiment.polarity
            )

if __name__ == '__main__':
    get_news_information(api=API)
