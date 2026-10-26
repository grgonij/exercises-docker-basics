import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = b"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hello from the cloud</title>
<style>
  :root { color-scheme: light dark; font-family: system-ui, sans-serif; }
  body { display: grid; place-items: center; min-height: 100vh; margin: 0; }
  main { text-align: center; padding: 2rem; }
</style>
</head>
<body>
<main>
  <h1>Hello from a container in the cloud!</h1>
  <p>DevOps with Docker, exercise 1.16</p>
</main>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(PAGE)


if __name__ == "__main__":
    # Cloud hosts like Render tell the app which port to use via $PORT
    port = int(os.environ.get("PORT", 8080))
    print(f"Listening on port {port}", flush=True)
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
