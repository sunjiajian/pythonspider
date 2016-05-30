import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '04_NBYH': '002142', '05_BJYH': '601169', '06_ZXZQ': '600030', '07_SXZQ': '002500', '08_HSDZ': '600570', '09_JZGF': '600446', '10_HJGF': '300368', '11_XBHJ': '601069', '12_CFHJ': '600988', '13_BLL_': '002601', '14_CDZS': '002253', '15_ZKCD': '300496', '16_THS_': '300033', '17_ASD_': '002416', '18_ZLGF': '002431', '19_AFDM': '002292', '20_HWKJ': '002362', '21_ZGZC': '601766', '22_DFCF': '300059', '23_ESSW': '002195', '24_YHRJ': '150019', '25_FDCB': '150118', '26_CYBB': '150153', '27_ZQB_': '150172', '28_HLWB': '150195', '29_YSB_': '150197', '30_CMB_': '150204', '31_GFB_': '150206', '32_XNCB': '150212', '33_WJRB': '150332'}

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
