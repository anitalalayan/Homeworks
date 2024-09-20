from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from messages.message import Message
    from users.user import User

class Conversation:
    def __init__(self, participants: List['User'])->None:
        self._participants = participants
        self._message_history:List[Message] = []

    def add_message(self, message: 'Message')->None:
        self._message_history.append(message)

    def add_user(self, user: 'User')->None:
        self._participants.append(user)

    def get_messages(self) -> List['Message']:
        return self._message_history

