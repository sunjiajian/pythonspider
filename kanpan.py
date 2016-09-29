import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01-----上指': 'sh', '02-----深指': 'sz', '03-----创指': 'cyb', '10--创业板B': '150153', '11--网金融B': '150332', '12--互联网B': '150195', '13----煤炭B': '150290', '14----钢铁B': '150288', '15----有色B': '150197', '19----证券B': '150172', '1A--房地产B': '150118', '1B--国企改B': '150210', '1C--新能车B': '150212', '1D----国防B': '150206', '20-中信证券': '600030', '22-西部证券': '002673', '23-第一创业': '002797', '2A----万科A': '000002', '31---乐视网': '300104', '3A-恒生电子': '600570'}

while 1:
    time.sleep(3)
    sub = 0
    codesdf = pandas.DataFrame(columns=('name', 'code', 'price', 'percent', 'amount'))
    for name, code in codes.items():
        try:
            df = tushare.get_realtime_quotes(code)
            percent = 100.0 * (float(df['price'][0]) - float(df['pre_close'][0]))/float(df['pre_close'][0])
            amount = float(df['amount'][0]) / 100000000
            # if float(df['amount'][0]) < 100000000:
            #     amount = float(df['amount'][0]) / 10000
            codesdf.loc[sub] = [name, code, df['price'][0], percent, amount]
            sub += 1
        except:
            pass
    print('------------------------------')
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print(codesdf.sort_values(by='name'))
