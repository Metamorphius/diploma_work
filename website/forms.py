from django import forms
from .models import *


class CryptForm(forms.Form):
    ticker = forms.CharField(max_length=255)
    time_frame = forms.CharField(max_length=255)