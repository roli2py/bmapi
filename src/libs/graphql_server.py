from libs.interfaces.graphql_server import IGraphQLServer
from libs.interfaces.resolvers import IResolvers

from ariadne import gql, QueryType, make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.explorer import ExplorerApollo

from textwrap import dedent

from collections.abc import Mapping


class GraphQLServer(IGraphQLServer):

    def __init__(self, resolvers_objs: Mapping[str, IResolvers]):
        schema = gql(dedent("""
            type Query {
                message: String
            }
        """))
        query = QueryType()

        object_types = (query,)

        for object_type in object_types:
            resolvers_obj = resolvers_objs[object_type.name]
            resolvers = resolvers_obj.get()
            for field, resolver in resolvers.items():
                query.set_field(field, resolver)

        executable_schema = make_executable_schema(schema, query)

        self.__app = GraphQL(executable_schema, debug=True, explorer=ExplorerApollo())

    @property
    def app(self) -> GraphQL:
        return self.__app
