from libs.interfaces.resolvers_interface import IResolversInterface
from libs.interfaces.resolvers import IResolvers


class ResolversInterface(IResolversInterface):

    def __init__(self, *resolvers_objs: IResolvers) -> None:
        self.__resolvers_objs = resolvers_objs

    def get(self) -> dict[str, IResolvers]:
        resolvers_dict = {
            resolvers.for_type: resolvers
            for resolvers in self.__resolvers_objs
        }
        return resolvers_dict
