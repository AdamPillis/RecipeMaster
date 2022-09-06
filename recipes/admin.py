from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    """To customise cateogry view via admin panel"""
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ['friendly_name']
    # use summernote_fields = ('content') for all textfield (instructions in each recipe)
    # use list_filter = ('', 'created_on')


admin.site.register(Category, CategoryAdmin)
