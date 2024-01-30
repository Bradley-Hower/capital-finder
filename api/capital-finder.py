from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    lex = dict(query_string_list)

    if 'capital' in lex:
      url = f'https://restcountries.com/v3.1/capital/'
      api_response = requests.get(url + lex['capital'])
      data = api_response.json()
      country = data["name"]["common"]
      message = f'{lex["capital"]} is the capital of {country}.'
    elif 'country' in lex:
      url = f'https://restcountries.com/v3.1/name/'
      api_response = requests.get(url + lex['country'])
      data = api_response.json()
      capital = data["capital"][0]
      message = f'{lex["country"]} is the capital of {capital}.'
    else:
      message = f'Nothing was found.'

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode('utf-8'))
    return
