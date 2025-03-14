from libs.interfaces.message_interface import IMessageInterface


class MessageInterface(IMessageInterface):

    def get(self) -> str:
        return "Здраствуйте! Это автоответчик. Сейчас роли занят."
