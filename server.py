from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import logging

class EverydayDummy(BaseHTTPRequestHandler):
    def _logRequestPayload(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        logging.info(data.decode('utf-8'))

    def _respond(self):
        self.send_response(200)
        self._sendCORSHeader()
        self.end_headers()

    def _sendCORSHeader(self):
        self.send_header('Access-Control-Allow-Origin', '*')

    def do_DELETE(self):
        self._logRequestPayload()
        self._respond()

    def do_GET(self):
        self._respond()

    def do_OPTIONS(self):
        self.send_response(200)
        self._sendCORSHeader()
        self.send_header('Access-Control-Allow-Methods', 'DELETE, GET, OPTIONS, POST, PUT')
        self.end_headers()
  
    def do_POST(self):
        self._logRequestPayload()
        self._respond()

    def do_PUT(self):
        self._logRequestPayload()
        self._respond()

def run(server_class=HTTPServer, handler_class=EverydayDummy, port=7049):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
