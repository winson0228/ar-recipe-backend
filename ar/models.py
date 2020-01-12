from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=2048)
    source = models.TextField()
    instructions = models.TextField()

class Ingredients(models.Model):
    name = models.CharField(max_length=2048, null=True)
    recipe = models.ForeignKey(Recipe, related_name="ingredients", on_delete=models.CASCADE)
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=2048, null=True)
