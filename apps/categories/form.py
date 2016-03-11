__author__ = 'javimuu'

from django import forms
from apps.categories.models import *


class CategoryForm(forms.ModelForm):
        """docstring for CategoryForm"""
        class Meta:
            model = Category
            fields = ['title', 'description']

