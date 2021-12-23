from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True, related_name="ingredients")

    def __str__(self):
        return self.name