import os
import logging
import requests
from flask import Flask, request
from flask_socketio import SocketIO, emit
from typing import Dict, Optional
import uuid
from logging_handler import LoggingHandler 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # what the hell is this... 
socketio = SocketIO(app, cors_allowed_origins="*")  # why do we use cors.. here.. and what if we

logger = LoggingHandler.getLogger('server_')

requests_to_socketid = {}
HEADERS = {'content-type': 'application/json'}
COMM_GATEWAY_URL = 'http://localhost:8080/user-message/jovensalud_1133556'


@socketio.on('connect')
def on_connect():
    logger.debug('****** connected client')


@socketio.on('disconnect')
def on_disconnect():
    logger.debug(f"****** User disconnected from socketIO endpoint.")

@socketio.on_error_default
def default_error_handler(e):
    logger.error('****** error occured ' + str(e))
    

@socketio.on('client_first')
def on_c1(data):
    logger.debug('first ' + data)
      
    try:
        logger.info("sending to comm server") 
        # TODO : make it async call
        r = requests.get(url=COMM_GATEWAY_URL, headers=HEADERS, json=data)
        logger.info("commgateway.. just responded for request : {}".format(r))

    except Exception as e:
        logger.error("error in sending to commgateway rasa..")
        logger.error(e)


    socketio.emit('server_second', 'response back from server')


@socketio.on('bot_message_came')
def on_c1(data):
    logger.debug('bot message came back from somewhere... ' + data)      

    # socketio.emit('server_second', 'response back from server')



if __name__ == '__main__':
    socketio.run(app, host='localhost', port=7000, debug=True, log_output=True, use_reloader=True)
    
