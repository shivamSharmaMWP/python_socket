import socketio
from logging_handler import LoggingHandler 

from flask import Flask
app = Flask(__name__)

logger = LoggingHandler.getLogger('comm_server_')


# preparing socket client here 

sio = socketio.Client(reconnection=True, reconnection_attempts=60, reconnection_delay=1)
class Staticc:
    connectivity_status = None

@sio.on('server_second')
def on_message(data):
    print('done ending the flow !' + data)
    

@sio.event
def connect():
    Staticc.connectivity_status = True
    print("comm connected!" + str(Staticc.connectivity_status))
    # sio.emit('client_first', 'hi')

@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    Staticc.connectivity_status = False
    print("I'm disconnected!" + str(Staticc.connectivity_status))



# logic.. if could't not connect then no issue. will try it in future.

try:     # reconnecting
    sio.connect('http://d_server:7000')
    # sio.wait()
except Exception as e:
    logger.exception("error in connecting first" + e)





@app.route("/")
def index():
    return """
        Welcome to my website!<br /><br />
        <a href="/hello">Go to hello world</a>
    """

@app.route("/hello")
def hello():
    return """
        Hello World!<br /><br />
        <a href="/">Back to index</a>
    """


@app.route('/user-message/<userid>')
def user(userid):
    logger.debug(" i am processing here.." + userid)
    logger.error(" and i am done.")
    return "user id " + userid + " processed successfully"

@app.route('/bot-message/<botid>')
def bott(botid):
    logger.debug(" bot processed here .." + botid + str(Staticc.connectivity_status))
    if Staticc.connectivity_status == True:
        logger.debug(" connection is still open")
    else: 
        logger.debug(" connection is closed now.. writing logic for reconnecting")

        try:     # reconnecting
            sio.connect('http://d_server:7000')
        except Exception as e:
            logger.exception("error in reconnecting" + str(e))

        logger.debug('simple connect statement, now sending data')
    
    sio.emit('bot_message_came', 'something detected' + botid)

    logger.error(" and bot is done.")
    return "bot id " + botid + " has been processed successfully by bot"
    


if __name__ == '__main__':
    # Will make the server available externally as well
    app.run(host='d_comm', port=8080)