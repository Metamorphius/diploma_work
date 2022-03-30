import requests

def get_dc_data(function, symbol, market, apikey):
    url = f'https://www.alphavantage.co/query?function={function}' \
          f'&symbol={symbol}&market={market}&interval=5min&apikey={apikey}'

    r = requests.get(url)

    data = r.json()
    key = 'Time Series (' + function.replace('_', ' ').title() + ')'

    return data[key]

