import json

import pytest

from cmd_chat.server.models import Message
from cmd_chat.server.services import _generate_new_message, _generate_update_payload


@pytest.mark.asyncio
async def test_generate_new_message():
    msg = await _generate_new_message("hello world")
    assert isinstance(msg, Message)
    assert msg.message == "hello world"


@pytest.mark.asyncio
async def test_generate_update_payload():
    messages = [Message(message="msg1"), Message(message="msg2")]
    users = {"127.0.0.1, User1": b"key1", "127.0.0.1, User2": b"key2"}

    payload = await _generate_update_payload(messages, users)
    data = json.loads(payload)

    assert "messages" in data
    assert "users_in_chat" in data
    assert len(data["messages"]) == 2
    assert "127.0.0.1, User1" in data["users_in_chat"]
