import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '10_HLWB': '150195', '11_WJRB': '150332', '12_GQGB': '150210', '13_GFB_': '150206', '14_YSB_': '150197', '15_CYBB': '150153', '16_ZQB_': '150172', '17_XNCB': '150212', '20_DYCY': '002797', '21_SXZQ': '002500', '22_XBZQ': '002673', '23_ZXZQ': '600030', '30_WSKJ': '300017', '31_LSW_': '300104', '32_OFG_': '002456', '33_SNYS': '002024', '3A_HSDZ': '600570', '3B_MSTZ': '000609', '3C_DWZQ': '601555', '3D_SLH_': '002285', '3E_DFCF': '300059', '40_HJGF': '300368', '41_THS_': '300033', '43_ZKCD': '300496', '44_JZGF': '600446', '45_CDZS': '002253', '46_BFJT': '300431', '50_ZXKJ': '300101', '51_YXML': '601890', '52_ZHDK': '000738', '53_SDHJ': '600547', '54_HYGY': '603799', '55_YQZY': '601388', '56_GSYS': '600259', '60_BLL_': '002601', '61_HNHJ': '002155', '62_ZDXL': '002298'}

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
