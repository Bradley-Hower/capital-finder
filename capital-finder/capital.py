from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    country = dict(query_string_list)

    if capital in country:
      url = f'https://restcountries.com/v3.1/capital/{capital}'
      data = url.json()
      capital = data.name.common
      message = f'{capital} is the capital of {country}.'
    else:
      message = f'No country was found when searching for {capital}.'

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.werite(message.encode('utf-8'))
    return

    
    

