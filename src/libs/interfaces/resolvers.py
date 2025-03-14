from abc import ABCMeta, abstractmethod

from ariadne.types import Resolver

from collections.abc import Mapping


class IResolvers(metaclass=ABCMeta):

    @property
    @abstractmethod
    def for_type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get(self) -> Mapping[str, Resolver]:
        raise NotImplementedError
