from libs.interfaces.resolvers import IResolvers
from libs.interfaces.message_interface import IMessageInterface

from ariadne.types import Resolver


class QueryResolvers(IResolvers):
    __for_type = "Query"

    def __init__(self, message_interface: IMessageInterface) -> None:
        self.__message_interface = message_interface
    
    @property
    def for_type(self) -> str:
        return self.__for_type

    def __resolve_message(self, *_) -> str:
        message = self.__message_interface.get()
        return message

    def get(self) -> dict[str, Resolver]:
        return {
            "message": self.__resolve_message,
        }
