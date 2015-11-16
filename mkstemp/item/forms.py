from django import forms
from django.forms import ModelForm

from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'text', 'url', 'parent']
        widgets = {'parent': forms.HiddenInput()}
