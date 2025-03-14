from ariadne.asgi import GraphQL

from abc import ABCMeta, abstractmethod


class IGraphQLServer(metaclass=ABCMeta):
    
    @property
    @abstractmethod
    def app(self) -> GraphQL:
        raise NotImplementedError
