from django import forms
from .models import *


class CryptForm(forms.Form):
    ticker = forms.ModelChoiceField(queryset=DigitalCurrency.objects.only('ticker'))

class StockForm(forms.Form):
    ticker = forms.ModelChoiceField(queryset=Stock.objects.only('ticker'))