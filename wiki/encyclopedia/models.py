from django.db import models
from django import forms
from django.utils.safestring import mark_safe

# Create your models here.
class NewEntryForm(forms.Form):
    title = forms.CharField(max_length=64)
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'new_page_textarea', 'cols': 1, 'rows': 1}))
