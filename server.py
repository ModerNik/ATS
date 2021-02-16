from http.server import BaseHTTPRequestHandler, HTTPServer
import re
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        path = self.path
        if path == "/":
            path = "/index"

        print(path)

        try:
            if ".css" in path:
                self.send_header('Content-type', 'text/css; charset=cp1251')
                file  = open("html" + path, 'r')
            elif ".js" in path:
                self.send_header('Content-type', 'text/javascript')
                file = open("html" + path, 'r')
            elif ".png" in path:
                self.send_header('Content-type', 'image/png')
                file = open("html" + path, 'r')
            else:
                self.send_header('Content-type', 'text/html; charset=cp1251')
                file = open("html" + path + ".html", 'r')
            print(file)
        except FileNotFoundError:
            file  = open("html/404.html", 'r')

##        self.send_header('charset', 'utf-8')
        self.end_headers()
        message = file.read()
        file.close()
        self.wfile.write(bytes(message, "cp1251"))
        return

    def do_POST(self):
        self.send_response(301)
        self.send_header('Location','/support')
        self.end_headers()
        path = self.path
        #Обработчик логина
        if path == "/signin":
            content_len = int(self.headers.get('Content-Length'))
            post = self.rfile.read(content_len)
            print(post)
            post = re.split(r'\'+',str(post))[1]
            print(post)
            fields = re.split(r'[ \'\&=]+',str(post))
            print(fields)
            login = fields[1]
            password = fields[3]
            print(login)
            print(password)
        return


server = HTTPServer(('127.0.0.1', 8081), myHandler)
server.serve_forever()