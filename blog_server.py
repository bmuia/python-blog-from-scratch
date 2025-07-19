from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

HOST = '127.0.0.1' 
PORT = 7000

class BlogHandlerServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/posts':
            if os.path.exists('posts.json'):
                with open('posts.json', 'r') as f:
                    posts = json.load(f)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(posts).encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'posts.json not found')
            return

        # Serve index.html
        if self.path == '/':
            file_path = '/index.html'
        else:
            file_path = self.path.strip("/") 
        if os.path.exists(file_path):
            # Detect content type
            if file_path.endswith('.html'):
                content_type = 'text/html'
            elif file_path.endswith('.css'):
                content_type = 'text/css'
            elif file_path.endswith('.js'):
                content_type = 'application/javascript'
            else:
                content_type = 'text/plain'

            with open(file_path, 'rb') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')

# Run the server
if __name__ == '__main__':
    print(f"Server running at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), BlogHandlerServer)
    server.serve_forever()
