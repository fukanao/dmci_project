from django import forms
from django.forms import Form, ModelForm, IntegerField, CharField
from .models import DjangoTestCompo 


class CompoForm(forms.Form):
    product_name = forms.CharField(
        label='プロダクト名',
        required=False,
        max_length=100,
    )

    product_text = forms.CharField(
        label='プロダクトテキスト',
        required=True,
        max_length=500,
        widget=forms.Textarea,
    )
