from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Recipe, Ingredient, Linked_recipes


class CategoryAdmin(admin.ModelAdmin):
    """To customise cateogry view via admin panel"""
    list_display = (
        'name',
    )
    search_fields = ['name']
    # use summernote_fields = ('content') for all textfield (instructions in each recipe)
    # use list_filter = ('', 'created_on')


class IngredientAdmin(admin.ModelAdmin):
    """To customise ingredient view via admin panel"""
    list_display = (
        'recipe',
        'ingredient_name',
        'amount',
        'quantity_type',
    )
    search_fields = ['name']


class RecipeAdmin(SummernoteModelAdmin):
    """All recipes in admin panel"""
    list_display = (
        'category',
        'name',
        'prep_time',
        'cooking_time',
        'tools_required',
        'step_guide',
        'image',
    )
    search_fields = ['name']
    summernote_fields = ('tools_required', 'step_guide')


class Linked_recipesAdmin(admin.ModelAdmin):
    """To customise ingredient view via admin panel"""
    list_display = (
        'recipe',
        'linked_recipe',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Linked_recipes, Linked_recipesAdmin)

