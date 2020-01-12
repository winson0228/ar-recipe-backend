import django_filters
from .models import *

class IngredientsFilter(django_filters.FilterSet):
    class Meta:
        model = Ingredients
        fields = ['name']

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ['ingredients', 'name']
