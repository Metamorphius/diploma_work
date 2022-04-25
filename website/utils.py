import requests
import pandas as pd


def get_dc_data(function, symbol, market, apikey):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&market={market}&apikey={apikey}'

    r = requests.get(url)

    data = r.json()

    key = 'Time Series (' + function.replace('_', ' ').title() + ')'

    return data[key]


def convert_dc_data_to_df(data):
    df = pd.DataFrame.from_dict(data, orient='index')

    df = df.reset_index()

    df = df.rename(index=str, columns={df.columns[0]: "date", df.columns[1]: "openA",
                                       df.columns[2]: "openB", df.columns[3]: "highA",
                                       df.columns[4]: "highB", df.columns[5]: "lowA",
                                       df.columns[6]: "lowB", df.columns[7]: "closeA",
                                       df.columns[8]: "closeB", df.columns[9]: "volume",
                                       df.columns[10]: "mcap", })

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['date'])

    df.openA = df.openA.astype(float)
    df.openB = df.openB.astype(float)
    df.highA = df.highA.astype(float)
    df.highB = df.highB.astype(float)
    df.lowA = df.lowA.astype(float)
    df.lowB = df.lowB.astype(float)
    df.closeA = df.closeA.astype(float)
    df.closeB = df.closeB.astype(float)
    df.volume = df.volume.astype(float)
    df.mcap = df.mcap.astype(float)

    return df