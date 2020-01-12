from graphene import List, InputObjectType, String

class RecipeInputType(InputObjectType):
    name = List(String)
