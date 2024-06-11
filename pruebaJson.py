import json
import http.server
import socketserver
from typing import Tuple
from http import HTTPStatus

class manejador(http.server.SimpleHTTPRequestHandler):

    def _init_(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        super()._init_(request, client_address, server)

    @property
    def contestador(self):
        return json.dumps({"message": "Funciono"}).encode()

    def vigilante(self):
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(self.contestador))


if __name__ == "__main__":
    PORT = 8000
    # Create an object of the above class
    servidor_adso03 = socketserver.TCPServer(("0.0.0.0", PORT), manejador)
    # Star the server
    print(f"Servidor escuchando por el puerto: {PORT}")
    servidor_adso03.serve_forever()