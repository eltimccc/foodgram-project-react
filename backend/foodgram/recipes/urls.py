from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import TagsView

router_v1 = DefaultRouter()

router_v1.register('tags', TagsView, basename='tags')


urlpatterns = [
    path('', include(router_v1.urls)),
]