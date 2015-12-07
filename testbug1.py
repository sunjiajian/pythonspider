import urllib.request
import json
import time
import datetime

codes = {'SZ000002': '02', 'SH000001': 'big bro'}

while 1:
    time.sleep(5)
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    for code, name in codes.items():
        he1 = {'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'http://xueqiu.com/S/%s' % code,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
                'Host': 'xueqiu.com',
                #'Connection':'keep-alive',
                #'Accept':'*/*',
                'cookie':'s=2dq712k3rx; xq_a_token=104d73a454a6ff79118019ac5a2722428ded10fb; xq_r_token=6a9d2d40660852a677475c3e23df8a04bb8284ce; Hm_lvt_1db88642e346389874251b5a1eded6e3=1449479272; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1449479909; __utmt=1; __utma=1.1802555965.1449479272.1449479272.1449479272.1; __utmb=1.4.10.1449479272; __utmc=1; __utmz=1.1449479272.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
               }
        url = "http://xueqiu.com/v4/stock/quote.json?code=%s&_=%s" % (code, int(time.time()))
        req = urllib.request.Request(url, headers=he1)
        data = urllib.request.urlopen(req).read().decode('UTF-8')
        js_data = json.loads(data)
        print(js_data[code]['current'], '\t', end='')
        print(js_data[code]['percentage'], '\t', end='')
        print(name)
