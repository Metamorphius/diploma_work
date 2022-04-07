from django import forms
from .models import *

choices = (('DIGITAL_CURRENCY_DAILY', 'Daily'),
           ('DIGITAL_CURRENCY_WEEKLY', 'Weekly'),
           ('DIGITAL_CURRENCY_MONTHLY', 'Monthly'),
           )

class CryptForm(forms.Form):
    ticker = forms.ModelChoiceField(queryset=DigitalCurrency.objects.only('ticker'))
    time_frame = forms.ChoiceField(label='Layout', choices=choices)
