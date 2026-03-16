from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATUC_DIR = BASE_DIR / "static"


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self, STATIC_DIR):
        templates_map = {
            '/': 'index.html',
            '/orders/': 'orders.html',
            '/categories/': 'categories.html'
        }

        template_name = templates_map.get(self.path)
        if template_name:
            template_path = TEMPLATES_DIR / template_name
            if not template_path.exists():
                self.send_error(404, "Template not found")
                return

            data = template_path.read_bytes()

            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(data)
        elif self.path.startswith("/static/"):
            # Тут делаем распаковку в список, чтобы избавиться от начального префикса /static/
            _, _, *static_path_list = self.path.split("/")
            static_path = STATIC_DIR.joinpath(*static_path_list)
            if not static_path.exists():
                self.send_error(404, "Static file not")
                return

            data = static_path.read_bytes()

            self.send_response(200)

            # Если есть другие типы данных в /static/,
            if static_path.name.endswith(".css"):
                self.send_header("Content-Type", "text/css")

            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_error(404)


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
