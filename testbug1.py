import urllib.request
import json
import time
import datetime
import tushare as ts

codes = {'SZ000002': '02', 'SZ000996': 'zq', 'SH000001': 'big bro'}

lhb = ts.top_list('2015-12-08')
print(lhb)

while 1:
    time.sleep(5)
    print('------------------------------')
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    for code, name in codes.items():
        he1 = {'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://xueqiu.com/S/%s' % code,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
                'Host': 'xueqiu.com',
                #'Connection':'keep-alive',
                #'Accept':'*/*',
                'cookie':'s=2dq712k3rx; xq_a_token=b091de3cd9721c7dd67d4115f609f42a95a6200a; xq_r_token=97ad548663a06fad5d7e0f733f67a89797d1d945; __utmt=1; __utma=1.1802555965.1449479272.1449479272.1449540187.2; __utmb=1.4.10.1449540187; __utmc=1; __utmz=1.1449479272.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1449479272,1449540187; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1449541963'
               }
        url = "http://xueqiu.com/v4/stock/quote.json?code=%s&_=%s" % (code, int(time.time()))
        req = urllib.request.Request(url, headers=he1)
        data = urllib.request.urlopen(req).read().decode('UTF-8')
        js_data = json.loads(data)
        print(js_data[code]['current'], '\t', end='')
        print(js_data[code]['percentage'], '\t\t', end='')
        print(name)
