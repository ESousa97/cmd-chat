import json

from sanic import Websocket

from cmd_chat.server.models import IncomingMessage, Message


async def _get_bytes_and_serialize(ws: Websocket) -> IncomingMessage:
    try:
        data = json.loads(await ws.recv())
        return IncomingMessage(**data)
    except Exception:
        return IncomingMessage()


async def _generate_new_message(message: str) -> Message:
    return Message(message=message)


async def _generate_update_payload(memory_msgs: list[Message], users_structure: dict) -> str:
    return json.dumps(
        {
            "messages": [i.message for i in memory_msgs],
            "users_in_chat": list(users_structure.keys()),
        }
    )
