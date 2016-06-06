import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '04_HLWB': '150195', '05_WJRB': '150332', '06_CYBB': '150153', '07_ZQB_': '150172', '08_YSB_': '150197', '09_XNCB': '150212', '10_DYCY': '002797', '11_SXZQ': '002500', '12_XBZQ': '002673', '13_ZXZQ': '600030', '14_HJGF': '300368', '15_THS_': '300033', '16_ZKCD': '300496', '17_DFCF': '300059', '18_LSW_': '300104', '19_HSDZ': '600570', '20_JZGF': '600446', '21_CDZS': '002253', '22_SNYS': '002024', '23_KDXF': '002230'}

while 1:
    time.sleep(3)
    sub = 0
    codesdf = pandas.DataFrame(columns=('name', 'price', 'percent', 'amount'))
    for name, code in codes.items():
        try:
            df = tushare.get_realtime_quotes(code)
            percent = 100.0 * (float(df['price'][0]) - float(df['pre_close'][0]))/float(df['pre_close'][0])
            amount = float(df['amount'][0]) / 100000000
            # if float(df['amount'][0]) < 100000000:
            #     amount = float(df['amount'][0]) / 10000
            codesdf.loc[sub] = [name, df['price'][0], percent, amount]
            sub += 1
        except:
            pass
    print('------------------------------')
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print(codesdf.sort_values(by='name'))
