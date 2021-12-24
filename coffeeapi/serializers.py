from rest_framework import serializers
from .models import (
    Coffee
)


class CoffeeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Coffee
        fields = ('name', 'description', 'ingredients')

    def get_ingredients(self, obj):
        ingredients = []
        qs = obj.ingredients.all()
        if qs:
            for item in qs:
                ingredients.append(item.name)

        return ingredients