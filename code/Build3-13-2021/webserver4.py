
import io
import socketserver
from threading import Condition
from http import server
run = True

PAGE="""\
<!DOCTYPE html>
<html lang="en-us">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Unity WebGL Player | Pat 2.0</title>
    <link rel="shortcut icon" href="TemplateData/favicon.ico">
    <link rel="stylesheet" href="TemplateData/style.css">
  </head>
  <body>
    <div id="unity-container" class="unity-desktop">
      <canvas id="unity-canvas"></canvas>
      <div id="unity-loading-bar">
        <div id="unity-logo"></div>
        <div id="unity-progress-bar-empty">
          <div id="unity-progress-bar-full"></div>
        </div>
      </div>
      <div id="unity-footer">
        <div id="unity-webgl-logo"></div>
        <div id="unity-fullscreen-button"></div>
        <div id="unity-build-title">Pat 2.0</div>
      </div>
    </div>
    <script>
      var buildUrl = "Build";
      var loaderUrl = "/Pat2.0.loader.js";
      var config = {
        dataUrl: "/Pat2.0.data.br",
        frameworkUrl: "/Pat2.0.framework.js.br",
        codeUrl: "/Pat2.0.wasm.br",
        streamingAssetsUrl: "StreamingAssets",
        companyName: "SoundMotion",
        productName: "Pat 2.0",
        productVersion: "1.0",
      };
      var container = document.querySelector("#unity-container");
      var canvas = document.querySelector("#unity-canvas");
      var loadingBar = document.querySelector("#unity-loading-bar");
      var progressBarFull = document.querySelector("#unity-progress-bar-full");
      var fullscreenButton = document.querySelector("#unity-fullscreen-button");
      if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        container.className = "unity-mobile";
        config.devicePixelRatio = 1;
      } else {
        canvas.style.width = "960px";
        canvas.style.height = "600px";
      }
      loadingBar.style.display = "block";
      var script = document.createElement("script");
      script.src = loaderUrl;
      script.onload = () => {
        createUnityInstance(canvas, config, (progress) => {
          progressBarFull.style.width = 100 * progress + "%";
        }).then((unityInstance) => {
          loadingBar.style.display = "none";
          fullscreenButton.onclick = () => {
            unityInstance.SetFullscreen(1);
          };
        }).catch((message) => {
          alert(message);
        });
      };
      document.body.appendChild(script);
    </script>
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
            self.send_header('content-type', 'text/html')
            self.send_header('content-length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/TemplateData/style.css':
            f=open('/home/pi/server/TemplateData/style.css')
            self.send_response(200)
            self.send_header('Ccntent-type', 'text/css')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(bytes(f.read(), 'utf-8'))
            f.close
        elif self.path == '/Pat2.0.loader.js':
            f=open('/home/pi/server/Pat2.0.loader.js')
            self.send_response(200)
            self.send_header('content-type', 'application/javascript')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(bytes(f.read(), 'utf-8'))
            f.close
        elif self.path == '/Pat2.0.data.br':
            f=open('/home/pi/server/Pat2.0.data.br', 'rb')
            self.send_response(200)
            self.send_header('content-type', 'application/javascript')
            self.send_header('application', 'soundmotion')
            self.send_header('content-encoding', 'brotli')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/Pat2.0.framework.js.br':
            f=open('/home/pi/server/Pat2.0.framework.js.br', 'rb')
            self.send_response(200)
            self.send_header('content-type', 'application/javascript')
            self.send_header('application', 'soundmotion')
            self.send_header('content-encoding', 'brotli')
            #self.send_header('content-length', str(len(f)))
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/Pat2.0.wasm.br':
            f=open('/home/pi/server/Pat2.0.wasm.br', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'application')
            self.send_header('application', 'soundmotion')
            self.send_header('content-encoding', 'brotli')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/TemplateData/fullscreen-button.png':
            f=open('/home/pi/server/TemplateData/fullscreen-button.png', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'imag/png')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close            
        elif self.path == '/TemplateData/webgl-logo.png':
            f=open('/home/pi/server/TemplateData/webgl-logo.png', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/TemplateData/progress-bar-full-dark.png':
            f=open('/home/pi/server/TemplateData/progress-bar-full-dark.png', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/TemplateData/progress-bar-empty-dark.png':
            f=open('/home/pi/server/TemplateData/progress-bar-empty-dark.png', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/TemplateData/unity-logo-dark.png':
            f=open('/home/pi/server/TemplateData/unity-logo-dark.png', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        elif self.path == '/TemplateData/favicon.ico':
            f=open('/home/pi/server/TemplateData/favicon.ico', 'rb')
            self.send_response(200)
            self.send_header('Content-Type', 'image')
            self.send_header('application', 'soundmotion')
            self.end_headers()
            self.wfile.write(f.read())
            f.close
        else:
            print("path to file not found: " + self.path)
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
