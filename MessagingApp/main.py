from datetime import datetime
from users.user import User
from messages.message import Message, TextMessage, MultimediaMessage

def main():

    ani = User("Ani", "ani@example.com")
    dave = User("Dave", "dave@example.com")

    conversation = ani.create_conversation(dave)

    text_message = TextMessage(sender=ani, conversation=conversation, content="Hello, Dave!", timestamp=datetime.now())
    ani.send_message(text_message, conversation)

    dave.receive_message(text_message)

    media_message = MultimediaMessage(sender=dave, conversation=conversation, file_path="image.jpg", media_type="Image", timestamp=datetime.now())
    dave.send_message(media_message, conversation)

    ani.receive_message(media_message)

    print("Conversation history:")
    ani.view_conversation_history(conversation)

if __name__ == "__main__":
    main()
