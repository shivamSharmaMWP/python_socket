import socketio
from logging_handler import LoggingHandler 
from flask import Flask
from utils.socket_static import SocketStatic

app = Flask(__name__)

logger = LoggingHandler.getLogger('comm_server_')


SocketStatic.initialize()



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
    logger.debug(" bot processed here .." + botid + str(SocketStatic.connectivity_status))
   
    status = SocketStatic.checkConnectivity()
    SocketStatic.SIO.emit('bot_message_came', 'something detected' + botid)

    logger.error(" and bot is done.")
    return "bot id " + botid + " has been processed successfully by bot"
    


if __name__ == '__main__':
    # Will make the server available externally as well
    app.run(host='d_comm', port=8080)