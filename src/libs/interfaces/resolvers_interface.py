from abc import ABCMeta, abstractmethod

from libs.interfaces.resolvers import IResolvers

from collections.abc import Mapping


class IResolversInterface(metaclass=ABCMeta):

    @abstractmethod
    def get(self) -> Mapping[str, IResolvers]:
        raise NotImplementedError
