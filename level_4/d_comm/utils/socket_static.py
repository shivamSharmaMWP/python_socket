import os
import socketio
from logging_handler import LoggingHandler

logger = LoggingHandler.getLogger('comm_server_')


class SocketStatic: 
    SIO = None
    connectivity_status = None

    def initialize():

        sio = socketio.Client(reconnection=True, reconnection_attempts=60, reconnection_delay=1)
        
        @sio.on('server_second')
        def on_message(data):
            print('done ending the flow !' + data)
            

        @sio.event
        def connect():
            SocketStatic.connectivity_status = True
            print("comm connected!" + str(SocketStatic.connectivity_status))
            # sio.emit('client_first', 'hi')

        @sio.event
        def connect_error():
            print("The connection failed!")

        @sio.event
        def disconnect():
            SocketStatic.connectivity_status = False
            print("I'm disconnected!" + str(SocketStatic.connectivity_status))


        try:
            sio.connect('http://d_server:7000')
            # sio.wait()
        except Exception as e:
            logger.exception("error in connecting first" + e)

        SocketStatic.SIO = sio


    def checkConnectivity():
                
        if SocketStatic.connectivity_status == True:
            logger.debug(" connection is still open")
        else: 
            logger.debug(" connection is closed now.. writing logic for reconnecting")

            try:     # reconnecting
                SocketStatic.SIO.connect('http://d_server:7000')
            except Exception as e:
                logger.exception("error in reconnecting" + str(e))

            logger.debug('Connected again !!, now sending data')