from rest_framework import serializers
from .models import Tags, Ingredient


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('__all__')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('__all__')