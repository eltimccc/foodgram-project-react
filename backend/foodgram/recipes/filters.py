from django_filters import rest_framework as django_filters

from recipes.models import Recipe


class RecipeFilter(django_filters.FilterSet):
    """Фильтр рецептов."""

    author = django_filters.CharFilter(field_name="author__id", lookup_expr="icontains")
    tags = django_filters.AllValuesMultipleFilter(field_name="tags__slug")
    is_favorited = django_filters.BooleanFilter(method="filter_is_favorited")
    is_in_shopping_cart = django_filters.BooleanFilter(
        method="filter_is_in_shopping_cart"
    )

    class Meta:
        model = Recipe
        fields = ("author", "tags", "is_favorited", "is_in_shopping_cart")

    def filter_is_favorited(self, queryset, name, value):
        if value:
            return queryset.django_filters(favorite_recipe__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.django_filters(cart_recipe__user=self.request.user)
        return queryset


class IngredientSearchFilter(django_filters.SearchFilter):

    search_param = "name"
