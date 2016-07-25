import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '10_HLWB': '150195', '11_WJRB': '150332', '12_FDCB': '150118', '20_ZXZQ': '600030', '22_XBZQ': '002673', '2A_WKA_': '000002', '2B_BLDC': '600048', '30_WSKJ': '300017', '33_SNYS': '002024', '3A_HSDZ': '600570', '3B_MSTZ': '000609'}

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
