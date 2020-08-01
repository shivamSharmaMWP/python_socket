import os
import socketio
from logging_handler import LoggingHandler

logger = LoggingHandler.getLogger('comm_server_')


class SocketStatic: 
    SIO = None
    connectivity_status = None

    _socket_url = 'http://nginx/'
    # _socket_url = 'http://d_server:7000'

    def initialize():

        sio = socketio.Client(reconnection=True, reconnection_attempts=60, reconnection_delay=1)
        
        @sio.on('server_second')
        def on_message(data):
            logger.info('done ending the flow !' + data)
            

        @sio.event
        def connect():
            SocketStatic.connectivity_status = True
            logger.info("comm connected!" + str(SocketStatic.connectivity_status))
            # sio.emit('client_first', 'hi from comm_server side')
            # sio.emit('client_first', 'hi')

        @sio.event
        def connect_error():
            logger.error("The connection failed!")

        @sio.event
        def disconnect():
            SocketStatic.connectivity_status = False
            logger.error("I'm disconnected!" + str(SocketStatic.connectivity_status))


        try:
            sio.connect(SocketStatic._socket_url)
            # sio.wait()
        except Exception as e:
            logger.exception("error in connecting first" + str())

        SocketStatic.SIO = sio


    def checkConnectivity():
        if SocketStatic.connectivity_status == None:
            SocketStatic.initialize()
        elif SocketStatic.connectivity_status == True:
            logger.info(" connection is still open")
        else: 
            logger.error(" connection is closed now.. writing logic for reconnecting")

            try:     # reconnecting
                SocketStatic.SIO.connect(SocketStatic._socket_url)
            except Exception as e:
                logger.exception("error in reconnecting" + str(e))

            logger.debug('Connected again !!, now sending data')