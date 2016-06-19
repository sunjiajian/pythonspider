import urllib.request
import json
import time
import datetime
import tushare
import pandas

codes = {'01_SH': 'sh', '02_SZ': 'sz', '03_CYB': 'cyb', '10_HLWB': '150195', '11_WJRB': '150332', '12_GFB_': '150206', '13_YSB_': '150197', '14_CYBB': '150153', '15_ZQB_': '150172', '16_XNCB': '150212', '20_DYCY': '002797', '21_SXZQ': '002500', '22_XBZQ': '002673', '23_ZXZQ': '600030', '24_HJGF': '300368', '25_THS_': '300033', '26_ZKCD': '300496', '27_DFCF': '300059', '28_LSW_': '300104', '29_HSDZ': '600570', '2A_JZGF': '600446', '2B_CDZS': '002253', '2C_SNYS': '002024', '2D_KDXF': '002230', '30_ZXKJ': '300101', '31_YXML': '601890', '32_ZHDK': '000738', '33_SDHJ': '600547', '34_HYGY': '603799', '35_YQZY': '601388', '36_GSYS': '600259', '40_BLL_': '002601', '41_HNHJ': '002155', '42_ZDXL': '002298', '50_TRXN': '002218', '51_DLDC': '002606', '52_HHKJ': '002645', '53_YXQC': '002607', '54_XLSY': '002105', '55_FZDJ': '002196', '56_CYNM': '002477'}

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
