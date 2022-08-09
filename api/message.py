from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import self as self


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        message = "please input a correct name"
        self.wfile.write(message.encode())
        return
