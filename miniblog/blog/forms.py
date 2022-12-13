import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CreateCommentForm(forms.Form):
    description = forms.CharField(
        help_text='Enter comment about blog here.')

    def clean_description(self):
        data = self.cleaned_data['description']

        return data
