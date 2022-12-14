from django import forms
from django.forms import Form, ModelForm, IntegerField, CharField
from .models import DjangoTestCompo 
from .models import DjangoTestMain 


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
    
    qty = forms.IntegerField(
            label='数量',
            initial=0,
            required=True,
    )

    unit_price = forms.IntegerField(
            label='単体価格',
            initial=0,
            required=True,
    )

class MainForm(forms.Form):
    quatation_meta_id = forms.CharField(
            label='見積もりID',
            required=True,
            max_length=100,
    )

    quatation_subject = forms.CharField(
            label = '見積もり名',
            #required = True,
            required = False,
            max_length = 100,
    )

    customer_id = forms.CharField(
            label = '顧客名',
            required = False,
            max_length = 100,
    )

class ConfirmForm(forms.Form):
    pass
