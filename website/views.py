from django.shortcuts import render
from django.views.generic import FormView
from .forms import *
from .models import *

class ChooseCrypt(FormView):
    form_class = CryptForm
    template_name = 'website/crypt_form.html'