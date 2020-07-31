import socketio
from logging_handler import LoggingHandler 

logger = LoggingHandler.getLogger('client_')

# standard Python
sio = socketio.Client()

@sio.on('server_second')
def on_message(data):
    print('done ending the flow !' + data)
    

@sio.event
def connect():
    print("I'm connected!")
    sio.emit('client_first', 'hi')

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

sio.connect('http://localhost:7000')
sio.wait()