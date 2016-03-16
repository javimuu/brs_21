from django import forms
from apps.categories.models import *
from apps.books.models import *

class CategoryForm(forms.ModelForm):
        """docstring for CategoryForm"""

        class Meta:
            model = Category
            fields = ['title', 'description']

            widgets = {
            'description': forms.widgets.Textarea(
                attrs={'class': 'materialize-textarea',}),
            }

class BookCategoryForm(forms.ModelForm):
        """docstring for CategoryForm"""

        class Meta:
            model = BookCategory
            fields = ['book', 'category']
