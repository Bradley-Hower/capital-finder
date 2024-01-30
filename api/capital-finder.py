from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    lex = dict(query_string_list)

    if 'capital' in country:
      url = f'https://restcountries.com/v3.1/capital/'
      country_response = requests.get(url + lex['capital'])
      data = country_response.json()
      country = data["name"]["common"]
      message = f'{["capital"]} is the capital of {country}.'
    elif 'country' in country:
      url = f'https://restcountries.com/v3.1/name/'
      capital_response = requests.get(url + lex['country'])
      data = capital_response.json()
      capital = data["capital"][0]
      message = f'{["country"]} is the capital of {capital}.'
    else:
      message = f'Nothing was found.'

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode('utf-8'))
    return
