import socket
import json
import pytest
import requests


class ApiClient():

    def __init__(self):
        self.url = 'http://myapp:8080'
        self.session = requests.Session()

    def login(self, log, psw):
        data = {
           "username": log,
           "password": psw,
           "submit": "Login"
        }
        resp = self.session.post(
            f'{self.url}/login',
            data=data
        )
        return resp

    def create_user(self, log, psw, email):
        data = {
           "username": log,
           "password": psw,
           "email": email
        }
        headers = {'Content-type': 'application/json'}
        resp = self.session.post(
            f'{self.url}/api/add_user',
            headers=headers,
            data=json.dumps(data)
        )
        return resp

    def delete_user(self, log):
        resp = self.session.get(f'{self.url}/api/del_user/{log}')
        return resp

    def block_user(self, log):
        resp = self.session.get(f'{self.url}/api/block_user/{log}')
        return resp

    def accept_user(self, log):
        resp = self.session.get(f'{self.url}/api/accept_user/{log}')
        return resp

    def status(self):
        resp = self.session.get(f'{self.url}/status')
        return resp.json()
