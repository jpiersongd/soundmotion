
import io
import socketserver
from threading import Condition
from http import server
run = True

PAGE="""\
<html>
<head>
<title>Raspberry Pi - basic web page</title>
</head>
<body>
<table style="width:50%">
    <tr>
        <th>blah</th>
        <th>blah</th>
        <th>blah</th>
    </tr>
    <tr>
        <th>blah</th>
        <th>blah</th>
        <th>blah</th>
    </tr>
        <tr>
        <th>blah</th>
        <th>blah</th>
        <th>blah</th>
    </tr>    
</body>
</html>
"""


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True



while run == True:

    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        run = True
