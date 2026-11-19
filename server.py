#!/usr/bin/env python3
"""Мини-апп «Сколько я трачу на интернеты». Только стандартная библиотека.
Запуск: python3 server.py  →  http://127.0.0.1:8765
Данные хранятся рядом, в data.json.
"""
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST, PORT = "127.0.0.1", 8765
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data.json")
INDEX = os.path.join(BASE, "index.html")
DEFAULT = {"rates": {"RUB": 1, "USD": 80, "EUR": 93}, "items": []}
lock = threading.Lock()


def load():
    if not os.path.exists(DATA):
        return DEFAULT
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)


def save(obj):
    tmp = DATA + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    os.replace(tmp, DATA)


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(INDEX, "rb") as f:
                self._send(200, f.read(), "text/html; charset=utf-8")
        elif self.path == "/api/data":
            with lock:
                body = json.dumps(load(), ensure_ascii=False).encode()
            self._send(200, body, "application/json; charset=utf-8")
        else:
            self._send(404, b"not found", "text/plain")

    def do_PUT(self):
        if self.path != "/api/data":
            return self._send(404, b"not found", "text/plain")
        try:
            n = int(self.headers.get("Content-Length", 0))
            obj = json.loads(self.rfile.read(n))
            assert isinstance(obj.get("items"), list)
        except Exception:
            return self._send(400, b"bad json", "text/plain")
        with lock:
            save(obj)
        self._send(200, b'{"ok":true}', "application/json")

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    url = f"http://{HOST}:{PORT}"
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Работает: {url}   (Ctrl+C — остановить)")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nПока!")
