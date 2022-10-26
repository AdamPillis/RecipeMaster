from django.db import models
from django.contrib.auth.models import User

QUANTITY_TYPE = (
    ("g", "g"),
    ("ml", "ml")
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
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """returns category name as string"""
        return self.name

    def get_friendly_name(self):
        """returns friendly name of category"""
        return self.friendly_name


class Ingredient(models.Model):
    """
    Class to for each ingredient, including pricing / gram
    """
    name = models.CharField(max_length=50, blank=False, null=True)
    quantity_type = models.CharField(choices=QUANTITY_TYPE, default=False, max_length=10)
    cost_per_quantity_type = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        """returns ingredient name as string"""
        return self.name

    def get_friendly_name(self):
        """returns friendly name of ingredient"""
        return self.friendly_name


# for image field, install pillow before migrations