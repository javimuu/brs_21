__author__ = 'javimuu'

from django import forms
from apps.books.models import *


class BookForm(forms.ModelForm):
    """ Form for Book Model """

    class Meta:
        model = Book
        fields = ['title', 'author', 'pages', 'publish_date', 'description', 'price', 'categories']

        widgets = {
            'description': forms.widgets.Textarea(
                attrs={'class': 'materialize-textarea',}
            ),
            'categories': forms.widgets.SelectMultiple(
                attrs={'multiple': "multiple"}
            ),
        }

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('User', None)
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['categories'].widget.choices = [(category.id, category.title) for category in Category.objects.all()]