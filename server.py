from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

port = 8100

handler = SimpleHTTPRequestHandler

with TCPServer(("", port), handler) as httpd:
	print("Serving handler on port",port)
	httpd.serve_forever()
