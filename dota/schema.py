import graphene
import heroes.schema


class Query(heroes.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
