from cmd_chat.server.models import IncomingMessage, Message


def test_message_model():
    msg = Message(message="Test 123")
    assert msg.message == "Test 123"


def test_incoming_message_model():
    msg = IncomingMessage(text="EncryptedData", username="John")
    assert msg.text == "EncryptedData"
    assert msg.username == "John"
    assert msg.action is None
