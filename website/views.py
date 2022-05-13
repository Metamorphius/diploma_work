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
from .neural_network import *



class ChooseCrypt(FormView):
    form_class = CryptForm
    template_name = 'website/crypt_form.html'


    def form_valid(self, form):
        self.request.session['selected_ticker'] = str(form.cleaned_data['ticker'])

        return super(ChooseCrypt, self).form_valid(form)

    def get_success_url(self):
        ticker = (self.request.session['selected_ticker']).lower()
        return reverse_lazy('crypt-page', kwargs={'slug_crypt': ticker})


class ChooseStock(FormView):
    form_class = StockForm
    template_name = 'website/stock_form.html'


    def form_valid(self, form):
        self.request.session['selected_ticker'] = str(form.cleaned_data['ticker'])

        return super(ChooseStock, self).form_valid(form)

    def get_success_url(self):
        ticker = (self.request.session['selected_ticker']).lower()
        return reverse_lazy('stock-page', kwargs={'slug_stock': ticker})


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


class StockPage(TemplateView):
    template_name = 'website/stock_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        symb = self.request.session['selected_ticker']

        dc_json = get_stok_data(symb, config('API_KEY'))

        df = convert_stock_data_to_df(dc_json)

        lstm_predict = train_lstm(df, symb, 100, 1, 10)

        source = pd.DataFrame(df, columns=['date', 'close'])
        source = source.to_dict('records')

        result = []

        for block in source:
            block['date'] = block['date'].strftime('%Y-%m-%d')
            result.append({
                'date': block['date'],
                'cost': block['close']
            }
            )

        context['data'] = json.dumps(result)

        date_df = pd.bdate_range(pd.Timestamp.today(), periods=10).tolist()
        date_predict = []

        for date in date_df:
            date_predict.append(date.strftime('%Y-%m-%d'))

        result_predict = []
        for i in range(10):
            result_predict.append({
                'date': date_predict[i],
                'cost': lstm_predict[i]
            }
            )

        context['predict_data'] = json.dumps(result_predict)

        return context