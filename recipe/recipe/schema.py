import graphene
from ar.schema import Query as ar_query
from ar.schema import Mutation as ar_mutation

class Query(ar_query,graphene.ObjectType):
    pass

class Mutation(ar_mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
