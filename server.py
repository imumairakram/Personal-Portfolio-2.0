import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Disable caching completely for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

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

        # Mock /_vercel/* routes for local development so it doesn't rewrite to index.html
        if self.path.startswith('/_vercel/'):
            self.send_response(204)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            return

        # SPA routing fallback: serve index.html for virtual routes
        clean_path = self.path.split('?')[0].lstrip('/')
        target_path = os.path.join(DIRECTORY, clean_path)
        
        if clean_path and not os.path.exists(target_path) and not clean_path.startswith(('assets/', '_vercel/')):
            self.path = '/index.html'

        return super().do_GET()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept')
        self.end_headers()

    def do_POST(self):
        if self.path == '/api/contact' or self.path.startswith('/api/contact?'):
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                import json, datetime
                msg_data = json.loads(post_data.decode('utf-8'))
                msg_data['received_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Append to messages.json in root
                msgs_file = os.path.join(DIRECTORY, 'messages.json')
                all_msgs = []
                if os.path.exists(msgs_file):
                    try:
                        with open(msgs_file, 'r', encoding='utf-8') as mf:
                            all_msgs = json.load(mf)
                    except Exception:
                        all_msgs = []
                all_msgs.append(msg_data)
                with open(msgs_file, 'w', encoding='utf-8') as mf:
                    json.dump(all_msgs, mf, indent=2)
                
                print("\n" + "=" * 60)
                print(" [NEW PORTFOLIO MESSAGE RECEIVED]")
                print(f" Name:    {msg_data.get('name')}")
                print(f" Email:   {msg_data.get('email')}")
                print(f" Subject: {msg_data.get('subject') or msg_data.get('_subject', 'No Subject')}")
                print(f" Message: {msg_data.get('message')}")
                print("=" * 60 + "\n")
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"success": true, "message": "Message saved successfully"}')
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(f'{{"success": false, "error": "{str(e)}"}}'.encode('utf-8'))
                return

def run():
    socketserver.TCPServer.allow_reuse_address = True
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
