from django.db import models
from django.contrib.auth.models import User

QUANTITY_TYPE = (
    ("g", "g"),
    ("ml", "ml")
    )

DIFFICULTY = (
    ("EASY", "EASY"),
    ("MEDIUM", "MEDIUM"),
    ("HARD", "HARD")
    )


class Category(models.Model):
    """
    Class to categorise RecipeMaster's desserts
    used in developement like search/filter functionality
    friendly_name is visual to the user instead of the name
    """
    class Meta:
        """To fix plural issue relating to django"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """returns category name as string"""
        return self.name


class Recipe(models.Model):
    """
    Model for every product hosted on Golf Mania
    Each need to include essential data such as name, description,
    category type, price and rest is optional.
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    prep_time = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    cooking_time = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    number_of_people = models.IntegerField(null=True, blank=False)
    difficulty = models.CharField(choices=DIFFICULTY, default=False, max_length=10)
    tools_required = models.TextField()
    step_guide = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """returning name of product which is displayed in admin"""
        return self.name


class Ingredient(models.Model):
    """
    Class to for each ingredient, including pricing / gram
    """
    recipe = models.ForeignKey(Recipe, null=True, blank=False, on_delete=models.CASCADE, related_name='ingredients')
    ingredient_name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    quantity_type = models.CharField(choices=QUANTITY_TYPE, default=False, max_length=10)

    def __str__(self):
        """returns ingredient name as string"""
        return self.ingredient_name


class Linked_recipes(models.Model):
    """
    x
    """
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE, related_name='recipe')
    linked_recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE, related_name='linked_recipe')