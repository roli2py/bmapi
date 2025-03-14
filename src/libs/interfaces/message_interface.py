from abc import ABCMeta, abstractmethod


class IMessageInterface(metaclass=ABCMeta):

    @abstractmethod
    def get(self) -> str:
        raise NotImplementedError
