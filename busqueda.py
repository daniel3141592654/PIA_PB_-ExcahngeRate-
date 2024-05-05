import requests #módulo externo instalado con pip
import json


def urlToDict(currency="USD")->dict:
    url = 'https://v6.exchangerate-api.com/v6/3c10a59bdcafd6990a473b46/latest/' + currency
    response = requests.get(url)
    data = response.json() 

    data = json.dumps(data)
    exchange = json.loads(data)

    return exchange['conversion_rates']
