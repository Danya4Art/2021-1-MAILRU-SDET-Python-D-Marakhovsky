import socket
import json
import settings

class Client():

    def __init__(self):
        self.host = settings.MOCK_HOST
        self.port = int(settings.MOCK_PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.1)
        self.sock.connect((self.host, self.port))

    def recieve(self):
        total_data = []
        while True:
            print('Data reading...')
            data = self.sock.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                self.sock.close()
                break
        data = ''.join(total_data).splitlines()
        return '\n'.join(data)


    def get_surname_by_name(self, name):
        params = f'/get_surname/{name}'
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'
        self.sock.send(request.encode())
        return self.recieve()

