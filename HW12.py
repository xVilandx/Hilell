import requests
import random
import csv


def get_raw_quote(how_quotes):
    list_quotes = []
    while len(list_quotes) < how_quotes:
        url = 'http://api.forismatic.com/api/1.0/'
        params = {'method': 'getQuote',
                  'format': 'json',
                  'lang': 'ru',
                  'key': random.randint(1, 999999)}
        responce = requests.get(url, params=params)
        quote_json = responce.json()
        if not quote_json['quoteAuthor'] == '':
            list_quote = [quote_json['quoteAuthor'], quote_json['quoteText'], quote_json['quoteLink']]
            list_quotes.append(list_quote)
    return list_quotes


def write_to_csv(file_csv, data):
    with open(file_csv, 'w') as csv_file:
        writer = csv.writer(csv_file,)
        writer.writerow(['Author', 'Quote', 'URL'])
        writer.writerows(sorted(data, key=lambda x: x[0]))


file_quotes_csv = 'quotes.csv'
list_author_quote_url = get_raw_quote(100)
write_to_csv(file_quotes_csv, list_author_quote_url)
