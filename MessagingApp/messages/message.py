from abc import ABC, abstractmethod
from datetime import datetime


class Message(ABC):
    def __init__(self, sender: 'User', conversation:'Conversation', timestamp: datetime):
        self._sender = sender
        self._conversation = conversation
        self._timestamp = datetime.now()

    @abstractmethod
    def display_content(self) -> None:
        ...

    @abstractmethod
    def get_message_type(self) -> str:
        ...


class TextMessage(Message):
    def __init__(self, sender: 'User', conversation:'Conversation', timestamp: datetime, content: str):
        super().__init__(sender, conversation, timestamp)
        self._content = content

    def display_content(self) -> None:
        print(f"[{self._timestamp}] {self._sender._name}: {self._content}")

    def get_message_type(self) -> str:
        return 'text'


class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation:'Conversation', timestamp: datetime, file_path: str, media_type: str ):
        super().__init__(sender, conversation, timestamp)
        self._media_type = media_type
        self._file_path = file_path

    def display_content(self) -> None:
        print(f"[{self._timestamp}] {self._sender._name} sent a {self._media_type}: {self._file_path}")

    def get_message_type(self) -> str:
        return self._media_type



