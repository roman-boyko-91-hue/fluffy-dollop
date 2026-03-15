from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATUC_DIR = BASE_DIR / "static"


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        templates_map = {
            '/': 'index.html',
            '/orders/': 'orders.html',
            '/categories/': 'categories.html'
        }

        file_path = templates_map.get(self.path)
        if file_path:
            full_path = TEMPLATES_DIR / file_path
            if full_path.exists():
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                with open(full_path, 'r', encoding='utf-8') as file:
                    self.wfile.write(file.read().encode('utf-8'))
            else:
                self.send_error(404, "File Not Found")
        else:
            self.send_error(404, "File Not Found")


def run(host: str, port: int) -> None:
    server = HTTPServer((host, port), MyServer)
    print(f"Server started http://{host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Server stopped.")
