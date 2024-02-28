import logging
from sanic import Sanic
from socketio import AsyncServer

from chatbox.constants import DEFAULT_CHAT_ROOM

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

app = Sanic(name="my_app")

server = AsyncServer(cors_allowed_origins="http://localhost:5173")  # To allow ui
server.attach(app)


@server.event
def connect(sid, _):
    logger.info(f"Someone new connected: {sid}")


@server.event
async def begin_chat(sid):
    logger.info(f"Someone new join the room {DEFAULT_CHAT_ROOM}: {sid}")
    await server.enter_room(sid, room=DEFAULT_CHAT_ROOM)


@server.event
async def exit_chat(sid):
    logger.info(f"Someone left the room {DEFAULT_CHAT_ROOM}: {sid}")
    await server.leave_room(sid, room=DEFAULT_CHAT_ROOM)


@server.event
def disconnect(sid):
    logger.info(f"Someone disconnected, dropping sessionId: {sid}")


@server.event
async def msg(sid, data):
    logger.info(f"Server received message from: {sid}, data: {data}")
    await server.emit(
        event="rsp",
        data=data,
        room=DEFAULT_CHAT_ROOM,
        skip_sid=sid,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
