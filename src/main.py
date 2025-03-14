from libs.graphql_server import GraphQLServer
from libs.message_interface import MessageInterface
from libs.resolvers.query_resolvers import QueryResolvers
from libs.resolvers_interface import ResolversInterface

from ariadne.asgi import GraphQL


class Main:

    def __init__(self) -> None:
        message_interface = MessageInterface()
        query_resolvers = QueryResolvers(message_interface)
        resolvers_interface = ResolversInterface(query_resolvers)
        resolvers_objs = resolvers_interface.get()
        graphql_server = GraphQLServer(resolvers_objs)
        self.__app = graphql_server.app
    
    @property
    def app(self) -> GraphQL:
        return self.__app
