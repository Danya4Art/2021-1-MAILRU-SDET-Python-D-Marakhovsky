import socket
import json
import settings

class Client():

    def __init__(self):
        self.host_mock = settings.MOCK_HOST
        self.port_mock = int(settings.MOCK_PORT)
        self.host = settings.APP_HOST
        self.port = int(settings.APP_PORT)

    def connect_mock(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.1)
        self.sock.connect((self.host_mock, self.port_mock))

    def connect_app(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.1)
        self.sock.connect((self.host, self.port))

    def recieve(self):
        total_data = []
        while True:
            data = self.sock.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.sock.close()
                break
        data = ''.join(total_data).splitlines()
        return '\n'.join(data)


    def get_surname_by_name(self, name):
        self.connect_mock()
        params = f'/get_surname/{name}'
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host_mock}\r\n\r\n'
        self.sock.send(request.encode())
        return self.recieve()

    def get_user_data(self, name):
        self.connect_app()
        params = f'/get_user/{name}'
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.sock.send(request.encode())
        return self.recieve()

    def create_new_user(self, name):
        self.connect_app()
        headers = 'POST {params} HTTP/1.1\r\n'\
        'Content-Type: application/json\r\n'\
        'Content-Length: {lenght}\r\n'\
        'Host: {host}\r\n'\
        'Connection: close\r\n'\
        '\r\n'
        body = {'name': name}
        body_json = json.dumps(body)
        header_bytes = headers.format(
            params='/add_user',
            lenght=len(body_json),
            host=self.host
            )
        payload = (header_bytes + body_json)
        self.sock.send(payload.encode())
        return self.recieve()

