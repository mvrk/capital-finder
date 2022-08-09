from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)
        country = query_dict.get("country")
        capital = query_dict.get("capital")

        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            data = requests.get(url).json()
            capital_name = data[0]["capital"][0]
            message = f"The capital of {country} is {capital_name}"
        elif capital:
            url = f"https://restcountries.com/v3.1/capital/{capital}"
            res = requests.get(url)
            data = requests.get(url).json()
            country_name = data[0]["name"]["official"]
            message = f"{capital} is the capital of {country_name}"
        else:
            message = "please input a correct name"

        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

        return
