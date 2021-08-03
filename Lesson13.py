import requests
import random


def get_raw_quote(lang='ru'):
    url = 'http://api.forismatic.com/api/1.0/'
    params = {'method': 'getQuote',
              'format': 'json',
              'lang': lang,
              'key': random.randint(1, 999999)}
    responce = requests.get(url, params=params)
    return responce.json()


def get_quote(raw_quote):
    return raw_quote['quoteText']


def get_author(raw_quote):
    return raw_quote['quoteAuthor']


for request_number in range(100):
    raw_quote = get_raw_quote()
    quote = get_quote(raw_quote)
    print(quote)

