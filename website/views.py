import json

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from decouple import config
from .forms import *
from .models import *
from .utils import *


class ChooseCrypt(FormView):
    form_class = CryptForm
    template_name = 'website/crypt_form.html'


    def form_valid(self, form):
        self.request.session['selected_ticker'] = str(form.cleaned_data['ticker'])

        return super(ChooseCrypt, self).form_valid(form)

    def get_success_url(self):
        ticker = (self.request.session['selected_ticker']).lower()
        return reverse_lazy('crypt-page', kwargs={'slug_crypt': ticker})


class CryptPage(TemplateView):
    template_name = 'website/crypt_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        symb = self.request.session['selected_ticker']

        dc_json = get_dc_data('DIGITAL_CURRENCY_DAILY', symb, 'USD', config('API_KEY'))

        df = convert_dc_data_to_df(dc_json)

        source = pd.DataFrame(df, columns=['date', 'openA'])
        source = source.to_dict('records')

        result = []

        for block in source:
            block['date'] = block['date'].strftime('%Y-%m-%d')
            result.append({
                'date': block['date'],
                'cost': block['openA']
                }
            )

        context['data'] = json.dumps(result)

        return context