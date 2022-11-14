from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Tags, Ingredient, Recipe
from .filters import IngredientSearchFilter, RecipeFilter
from .serializers import (TagsSerializer,
                          IngredientSerializer,
                          RecipeSerializer,
                          RecipesCreateSerializer)
from .pagination import LimitPageNumberPagination


class TagsView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = None


class IngredientView(viewsets.ReadOnlyModelViewSet):
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Ingredient.objects.all()
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)
    pagination_class = None


class RecipeView(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Recipe.objects.all()
    filterset_class = RecipeFilter
    pagination_class = LimitPageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH'):
            return RecipesCreateSerializer
        return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
