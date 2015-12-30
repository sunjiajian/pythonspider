import urllib.request
import json
import time
import datetime
import tushare as ts
import pandas

def code2str(cd):
    if cd < 10:
        scd = '00000%d' % cd
        return scd
    elif cd < 100:
        scd = '0000%d' % cd
        return scd
    elif cd < 1000:
        scd = '000%d' % cd
        return scd
    elif cd < 10000:
        scd = '00%d' % cd
        return scd
    elif cd < 100000:
        scd = '%d' % cd
        return scd
    else:
        scd = str(cd)
        return scd

days = {'day0': '2015-12-28', 'day1': '2015-12-29'}

# dfall = ts.get_today_all()
# dfall.to_excel('all.xlsx')
dfall = pandas.read_excel('all.xlsx')

for code in dfall.code:
    try:
        cd = code2str(code)
        hist = ts.get_hist_data(cd, '2015-12-28', '2015-12-29')
        mnd0 = float(hist['ma5'][0]) - float(hist['ma20'][0])
        mnd1 = float(hist['ma5'][1]) - float(hist['ma20'][1])
        if mnd0 < mnd1:
            print(cd, '----------------------------------------------------')
            # print(hist)
    except:
        pass

# lhb = ts.top_list(days['day0'])
# lhb.to_excel('test1.xlsx')
# print(len(lhb.index), len(lhb.columns))

# sub = 0

# n_data = pandas.DataFrame(columns=('n_open', 'n_close', 'n_high', 'n_low', 'n_p_change', 'n_turnover'))

# for code in lhb.code:
#     try:
#         data = ts.get_hist_data(code, days['day1'], days['day1'])
#         n_data.loc[sub] = [data['open'][0], data['close'][0], data['high'][0], data['low'][0], data['p_change'][0], data['turnover'][0]]
#         # print(n_data)
#     except:
#         n_data.loc[sub] = ['nan', 'nan', 'nan', 'nan', 'nan', 'nan']
#     sub += 1
#     print(sub)

# lhb = lhb.merge(n_data, left_index=True, right_index=True)
# print(lhb)
# lhb.to_excel('test1.xlsx')


# while 1:
#     time.sleep(5)
#     print('------------------------------')
#     print(datetime.datetime.now().strftime("%H:%M:%S"))
#     for code, name in codes.items():
#         he1 = {'X-Requested-With': 'XMLHttpRequest',
#                 'Referer': 'http://xueqiu.com/S/%s' % code,
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
#                 'Host': 'xueqiu.com',
#                 #'Connection':'keep-alive',
#                 #'Accept':'*/*',
#                 'cookie':'s=2dq712k3rx; xq_a_token=b091de3cd9721c7dd67d4115f609f42a95a6200a; xq_r_token=97ad548663a06fad5d7e0f733f67a89797d1d945; __utmt=1; __utma=1.1802555965.1449479272.1449479272.1449540187.2; __utmb=1.4.10.1449540187; __utmc=1; __utmz=1.1449479272.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1449479272,1449540187; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1449541963'
#                }
#         url = "http://xueqiu.com/v4/stock/quote.json?code=%s&_=%s" % (code, int(time.time()))
#         req = urllib.request.Request(url, headers=he1)
#         data = urllib.request.urlopen(req).read().decode('UTF-8')
#         js_data = json.loads(data)
#         print(js_data[code]['current'], '\t', end='')
#         print(js_data[code]['percentage'], '\t\t', end='')
#         print(name)
#