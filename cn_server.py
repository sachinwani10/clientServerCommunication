"""
Name: Sachin Ravindra Wani
Stud ID: 1001563321
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
# from time import sleep

HOST_NAME = "127.0.0.1"
PORT = 8000


class MyHandler(BaseHTTPRequestHandler):

    # def __init__(self, request, client_address, server):
    #     print("instance created")
    #     super().__init__(request, client_address, server)

    def do_HEAD(self, s):
        """
        function Sends headers to client
        :param s:
        :return:
        """
        file_name = self.path
        if file_name[0] == '/':
            file_name = file_name[1:]
        abort = False
        try:
            f = open(file_name, "r")
        except FileNotFoundError as err:
            f.close()
            self.send_error(404, "File Not Found")
            print(err)
            abort = True
        if not abort:
            s.send_response(200)
            s.send_header("content-type", "text/html")
            s.end_headers()

    def do_GET(self):
        """
        function to server the GET request
        :return: None
        """
        file_name = self.path
        if file_name[0] == '/':
            file_name = file_name[1:]
        abort = False
        try:
            f = open(file_name, "r")
        except FileNotFoundError as err:
            print(err)
            self.send_error(404, "File Not Found")
            print("Listening...")
            abort = True
        if not abort:
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            file_name = self.path
            print("Request: GET " + file_name)
            client_info = self.client_address
            print("Client Host: " + str(client_info[0]))
            print("Client Port: " + str(client_info[1]))
            try:
                data = f.read()
                self.wfile.write(data.encode())
            except FileNotFoundError:
                self.send_response(404)
                print(file_name + " Not Found")
            finally:
                # sleep(10)
                message = threading.currentThread().getName()
                print("Client is handled by: " + message)
                print("=======================================")
                print("Listening...")


if __name__ == "__main__":
    server_class = ThreadingHTTPServer
    # create socket, listen and accept incoming request
    httpd = server_class((HOST_NAME, PORT), MyHandler)
    print("Server Started!")
    print("Listening....")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server Stopped")
