from django.urls import include, path
from recipes.views import (CustomUserViewSet, IngredientView, RecipeView,
                           TagsView)
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register("tags", TagsView, basename="tags")
router_v1.register("ingredients", IngredientView, basename="ingredients")
router_v1.register("recipes", RecipeView, basename="resipes")
router_v1.register("users", CustomUserViewSet, basename="users")

urlpatterns = [
    path("", include(router_v1.urls)),
]
