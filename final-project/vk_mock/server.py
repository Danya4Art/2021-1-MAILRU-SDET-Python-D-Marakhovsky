import threading
from flask import Flask, jsonify, request
import json
import requests
import random

app = Flask(__name__)
USER_LIST = {}
user_id_seq = 100000000


@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "ok"})

@app.route('/new_user/<username>', methods=['POST'])
def create_new_user(username):
    global user_id_seq
    global USER_LIST
    answer = {}
    if username in USER_LIST.keys():
        answer['Status'] = '403 Forbidden'
        answer['Content-Type'] = 'application/json' 
        answer['Response'] = 'User already exist'
    else:
        USER_LIST[username] = user_id_seq
        user_id_seq += 1
        answer['Status'] = '200 OK'
        answer['Content-Type'] = 'application/json' 
        answer['vk_id'] = USER_LIST[username]
    return jsonify(answer)

@app.route('/vk_id/<username>', methods=['GET'])
def get_user_surname(username):
    answer = {}
    if username in USER_LIST.keys():
        answer['Status'] = '200 OK'
        answer['Content-Type'] = 'application/json' 
        answer['vk_id'] = USER_LIST[username]
    else:
        answer['Status'] = '404 Not Found'
        answer['Content-Type'] = 'application/json' 
        answer['Response'] = {}
    return jsonify(answer)

@app.route('/shutdown')
def shutdown():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()
    return jsonify({'msg': f'OK, exiting'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')