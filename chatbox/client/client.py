import logging
from socketio import Client

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

client = Client()


@client.event
def connect():
    client.emit("begin_chat")
    logger.info("I am connected")


@client.event
def rsp(data):
    logger.info(data)


@client.event
def disconnect():
    client.emit("exit_chat")
    logger.info("Client disconnected")


if __name__ == "__main__":
    client.connect("http://localhost:5000")
    client.emit("msg", "Hello i am client bob")
    client.wait()
