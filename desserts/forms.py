from django import forms
from home.widgets import CustomClearableFileInput
from desserts.models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    """
    Add recipe form
    """
    class Meta:
        """
        class refering to Recipe model and fields
        to include in form
        """
        model = Recipe
        fields = '__all__'
        summernote_fields = ('tools_required', 'step_guide')
        exclude = ('image_url',)
        # image field is linked with custom styled widget
        image = forms.ImageField(
            label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'name': 'Recipe Title',
            'prep_time': 'Preparation Time',
            'cooking_time': 'Cooking Time',
            'number_of_people': 'Number of portions',
            'difficulty': 'Difficulty',
            'tools_required': 'Tools Required',
            'step_guide': 'Step Guide',
            'image': 'Image',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black'
        self.fields[field].label = False


class IngredientForm(forms.ModelForm):
    """
    Add ingredient form
    """
    class Meta:
        """
        class refering to Recipe model and fields
        to include in form
        """
        model = Ingredient
        fields = [
            'ingredient_name',
            'amount',
            'quantity_type',
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'ingredient_name': 'Name',
            'amount': 'Amount',
            'quantity_type': 'Measure Type',
        }

        self.fields['ingredient_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'border-black'
        self.fields[field].label = False

