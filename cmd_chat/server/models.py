from pydantic import BaseModel


class Message(BaseModel):
    message: str


class IncomingMessage(BaseModel):
    text: str | None = None
    username: str | None = None
    action: str | None = None
