from typing import List
from messages.message import Message, TextMessage, MultimediaMessage
from messages.messagingmanager import MessagingManager
from convos.conversation import Conversation

class User(MessagingManager):
    def __init__(self, name:str, contact_info:str):
        self._name = name
        self._contact_info = contact_info
        self._conversations: List['Conversation'] = []

    def create_conversation(self, user:'User') -> 'Conversation':
        conversation = Conversation([self, user])
        self._conversations.append(conversation)
        user._conversations.append(conversation)
        return conversation

    def send_message(self, message:Message, conversation:'Conversation') -> None:
        conversation.add_message(message)

    def receive_message(self, message: 'Message') -> None:
        print(f"{self._name} received a message: {message.display_content()}")

    def manage_settings(self)->None:
        print("Manage settings")

    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        msg = conversation.get_messages()
        for message in msg:
            message.display_content()


    def get_conversations(self) -> List['Conversation']:
        return self._conversations


