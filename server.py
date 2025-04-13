import os
import logging
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def run_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = SimpleHTTPRequestHandler
    logging.info(f"Server is starting... Visit http://localhost:{PORT} to view your page.")

    try:
        with TCPServer(("", PORT), Handler) as httpd:
            logging.info(f"Serving at http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        logging.error("Server failed to start: %s", e)

if __name__ == "__main__":
    run_server()
