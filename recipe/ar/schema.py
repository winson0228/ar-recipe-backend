import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .filter import *
from .mutation import *
from .models import *
from .node import *
import re

LIST_OF_INGREDIENTS = ["apple", "orange", "banana"]

class Query(ObjectType):
    recipe = relay.Node.Field(RecipeNode)
    recipes = graphene.List(RecipeNode, names=graphene.List(graphene.String))

    ingredient = relay.Node.Field(IngredientsNode)
    ingredients = DjangoFilterConnectionField(IngredientsNode, filterset_class=IngredientsFilter)

    def resolve_recipes(self, info, names=None):
        if names:
            filtered_ingredients = []
            for ingred in LIST_OF_INGREDIENTS:
                regex = re.compile(f'*{ingred}*')
                for name in names:
                    if re.match(regex, name) and ingred not in filtered_ingredients:
                        filtered_ingredients.append(ingred)
                        break;
            return Recipe.objects.filter(ingredients__name__in=filtered_ingredients)
        return []

class Mutation(ObjectType):
    analyze_image = AzureAI.Field()
