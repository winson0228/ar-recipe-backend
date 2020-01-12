import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .filter import *
from .mutation import *
from .models import *
from .node import *

class Query(ObjectType):
    recipe = relay.Node.Field(RecipeNode)
    recipes = graphene.List(RecipeNode, names=graphene.List(graphene.String))

    ingredient = relay.Node.Field(IngredientsNode)
    ingredients = DjangoFilterConnectionField(IngredientsNode, filterset_class=IngredientsFilter)

    def resolve_recipes(self, info, names=None):
        if names:
            names = [word for name in names for word in name.split('.')]
            return Recipe.objects.filter(ingredients__name__in=names)
        return []

class Mutation(ObjectType):
    analyze_image = AzureAI.Field()
