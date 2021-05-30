import threading

from flask import Flask, jsonify, request

import settings

import json
import requests

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify({"surname": surname}), 200
    else:
        return jsonify({'msg': f'Surname for user {name} not fount'}), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify({'msg': f'OK, exiting'}), 200

@app.route('/rewrite/<name>', methods=['PUT'])
def rewrite_user_surname(name):
    new_surname = json.loads(request.data)['surname']
    if name in SURNAME_DATA.keys():
        surname = SURNAME_DATA[name]
        SURNAME_DATA[name] = new_surname
        data = jsonify({'name': name, 'surname': surname, 'new_surname': new_surname}), 200
    else:
        data = jsonify({'msg': f'Surname of user {name} is not foudn'}), 404
    return data

@app.route('/delete/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if name in SURNAME_DATA.keys():
        surname = SURNAME_DATA[name]
        SURNAME_DATA.pop(name)
        data = jsonify({'name': name, 'surname': surname}), 200
    else:
        data = jsonify({'msg': f'Surname of user {name} was not found'}), 404
    return data