from django.urls import path
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='website/index.html')),
    path('crypt/', ChooseCrypt.as_view(), name='crypt'),
    path('stock/', ChooseStock.as_view(), name='stock'),
    path('crypt/<slug:slug_crypt>', CryptPage.as_view(), name='crypt-page'),
    path('stock/<slug:slug_stock>', StockPage.as_view(), name='stock-page')
]