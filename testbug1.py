import urllib.request
import json

code = 'SZ000002'

he1 = {'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://xueqiu.com/S/SZ000004',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Host': 'xueqiu.com',
        #'Connection':'keep-alive',
        #'Accept':'*/*',
        'cookie':'s=2dq712k3rx; xq_a_token=104d73a454a6ff79118019ac5a2722428ded10fb; xq_r_token=6a9d2d40660852a677475c3e23df8a04bb8284ce; Hm_lvt_1db88642e346389874251b5a1eded6e3=1449479272; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1449479909; __utmt=1; __utma=1.1802555965.1449479272.1449479272.1449479272.1; __utmb=1.4.10.1449479272; __utmc=1; __utmz=1.1449479272.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
       }
url = "http://xueqiu.com/v4/stock/quote.json?code=SZ000004&_=1449480195843"
req = urllib.request.Request(url, headers=he1)
data = urllib.request.urlopen(req).read().decode('UTF-8')

jsdata = json.loads(data)
# print(jsdata)
# type(jsdata)
print(jsdata['SZ000004']['current'], end='\n')
print(jsdata['SZ000004']['net_assets'], end='\n')
