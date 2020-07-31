import os
import logging
import requests
from flask import Flask, request
from flask_socketio import SocketIO, emit
from typing import Dict, Optional
import uuid
from logging_handler import LoggingHandler 

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'  # what the hell is this... 
socketio = SocketIO(app)  # why do we use cors.. here.. and what if we

logger = LoggingHandler.getLogger('server_')

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
    socketio.emit('server_second', 'response back from server')

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=7000, debug=True, log_output=True, use_reloader=True)
    