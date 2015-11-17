from django import forms
from django.forms import ModelForm

from .models import Item
from .utils import is_valid_story_or_comment


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'text', 'url', 'parent']
        widgets = {'parent': forms.HiddenInput()}

    def clean(self):
        cleaned_data = super(ItemForm, self).clean()
        status, msg = is_valid_story_or_comment(cleaned_data)
        if not status:
            raise forms.ValidationError(msg)
        return cleaned_data
