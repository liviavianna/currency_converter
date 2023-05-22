import requests
from api_key import api_key

from_cr = input('Para:')
to_cr = input('De:')
amount = input('Valor:')
url = 'https://api.apilayer.com/exchangerates_data/convert?'

payload = { 
    'to': to_cr, 
    'from': from_cr, 
    'amount': amount 
}

headers= {
  'apikey': api_key
}

r = requests.request(
    'GET', 
    url, 
    headers = headers, 
    params = payload
)

print(r.text)
