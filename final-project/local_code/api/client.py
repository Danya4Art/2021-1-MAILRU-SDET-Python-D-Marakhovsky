import json
import pytest
import requests
import re
from requests.cookies import cookiejar_from_dict


class ApiClient():

    def __init__(self):
        self.url = 'http://127.0.0.1:8080'
        self.session = requests.Session()

    def find_cookies(self, all_cookies, cookies_names):
        pattern = r'Cookie (\w+)=(\S+)'
        find_all = re.findall(pattern, str(all_cookies))
        return [{'name': i[0], 'value': i[1]} for i in find_all if i[0] in cookies_names]

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
        print(resp)
        cookies_names = ['session']
        new_cookies_list = self.find_cookies(self.session.cookies, cookies_names)
        return new_cookies_list

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
