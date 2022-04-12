from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, View
from django.urls import reverse_lazy
from .forms import *
from .models import *



class ChooseCrypt(FormView):
    form_class = CryptForm
    template_name = 'website/crypt_form.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        self.request.session['selected_ticker'] = str(form.cleaned_data['ticker'])
        self.request.session['selected_time_frame'] = form.cleaned_data['time_frame']

        return super(ChooseCrypt, self).form_valid(form)

    def get_success_url(self):
        ticker = (self.request.session['selected_ticker']).lower()
        return reverse_lazy('crypt-page', kwargs={'slug_crypt': ticker})


class CryptPage(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Output')