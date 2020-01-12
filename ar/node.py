import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType

from .connections import *
from .models import *

class RecipeNode(DjangoObjectType):
    class Meta:
        model = Recipe
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection

class IngredientsNode(DjangoObjectType):
    class Meta:
        model = Ingredients
        interfaces = (relay.Node,)
        connection_class = ExtendedConnection
