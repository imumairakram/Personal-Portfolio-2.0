import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Handle /api/content route
        if self.path == '/api/content' or self.path.startswith('/api/content?'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            json_file = os.path.join(DIRECTORY, 'api_content.json')
            if os.path.exists(json_file):
                with open(json_file, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b'{}')
            return

        # SPA routing fallback: serve index.html for virtual routes
        clean_path = self.path.split('?')[0].lstrip('/')
        target_path = os.path.join(DIRECTORY, clean_path)
        
        if clean_path and not os.path.exists(target_path) and not clean_path.startswith('assets/'):
            self.path = '/index.html'

        return super().do_GET()

def run():
    server_address = ('', PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, PortfolioHandler)
    print("=" * 60)
    print(f" Portfolio Server running at http://localhost:{PORT}")
    print(f" Open http://localhost:{PORT} in your browser to view the site")
    print(" Press Ctrl+C to stop the server")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
