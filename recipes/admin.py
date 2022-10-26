from django.contrib import admin
from .models import Category, Ingredient


class CategoryAdmin(admin.ModelAdmin):
    """To customise cateogry view via admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ['friendly_name']
    # use summernote_fields = ('content') for all textfield (instructions in each recipe)
    # use list_filter = ('', 'created_on')


class IngredientAdmin(admin.ModelAdmin):
    """To customise ingredient view via admin panel"""
    list_display = (
        'name',
        'quantity_type',
        'cost_per_quantity_type',
    )
    search_fields = ['friendly_name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
