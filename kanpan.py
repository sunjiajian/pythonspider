import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '04_NBYH': '002142', '05_XBZQ': '002673', '06_YDDZ': '600602', '07_SSBA': '000019', '08_CXFZ': '000838', '09_ZJDR': '600113', '10_BYXC': '002297', '11_ZCFW': '600685', '12_YXML': '601890', '13_ZHDL': '600893', '14_ZHDK': '000738', '15_SHPT': '600680', '16_XBHJ': '601069', '17_CFHJ': '600988', '18_BLL_': '002601', '19_ZHTB': '002145', '20_CDZS': '002253', '21_ZKCD': '300496', '22_THS_': '300033', '23_ASD_': '002416', '24_ZLYL': '002431', '25_AFDM': '002292', '26_HWKJ': '002362', '27_CYB_': '150244', '28_HLWB': '150195', '29_YSB_': '150197', '30_ZQB_': '150172', '31_GFB_': '1502206', '32_XNCB': '150212', '33_FDCB': '150118', '34_CMB_': '150204', '35_GFB_': '150206'}

while 1:
    time.sleep(3)
    sub = 0
    codesdf = pandas.DataFrame(columns=('name', 'price', 'pre'))
    for name, code in codes.items():
        try:
            df = tushare.get_realtime_quotes(code)
            pre = 100.0 * (float(df['price'][0]) - float(df['pre_close'][0]))/float(df['pre_close'][0])
            codesdf.loc[sub] = [name, df['price'][0], pre]
            sub += 1
        except:
            pass
    print('------------------------------')
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print(codesdf.sort_values(by='name'))
