from django.contrib import admin
from .models import (
    Coffee,
    Ingredient
)

admin.site.register(Coffee)
admin.site.register(Ingredient)