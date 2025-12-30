#!/usr/bin/python3
"""
Task 03: Develop a simple API using Python's http.server module
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a simple API."""

    def _send_json(self, status_code, data):
        """Send a JSON response."""
        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def _send_text(self, status_code, text):
        """Send a plain text response."""
        response = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(
                200,
                {"name": "John", "age": 30, "city": "New York"}
            )
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            self._send_json(
                200,
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            )
        else:
            self._send_json(404, {"error": "Endpoint not found"})


def run_server(host="0.0.0.0", port=8000):
    """Start the HTTP server."""
    server = HTTPServer((host, port), SimpleAPIHandler)
    print(f"Server running on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
