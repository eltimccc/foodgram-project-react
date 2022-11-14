from django_filters import rest_framework as django_filters
from rest_framework import filters

# from recipes.models import Recipe, Tags


class IngredientSearchFilter(filters.SearchFilter):

    search_param = 'name'
