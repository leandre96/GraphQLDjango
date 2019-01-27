import graphene

import personal.schema
import second.schema


class Query(personal.schema.Query,second.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
