from django import forms
from .widgets import CustomClearableFileInput
from desserts.models import Category


class CategoryForm(forms.ModelForm):
    """
    Add category form
    """
    class Meta:
        """
        class refering to Category model and fields
        to include in form
        """
        model = Category
        fields = '__all__'
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
            'name': 'Category Name',
            'image_url': 'Category Image',
            'image': 'Category Image',
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

        