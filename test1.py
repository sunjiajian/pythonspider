import tushare as ts
import pandas
import xlrd

# bbd = ts.get_hist_data('000996', start='2014-08-28', end='2014-08-28')
# print(bbd)

bs = pandas.read_excel('all.xlsx')

# print(bs)

n_data = pandas.DataFrame(columns=('code', 'begin', 'end'))

sub = 0
for code in bs.code:
    try:
        print(sub)
        beginData = ts.get_hist_data(str(code), start='2015-08-28', end='2015-08-28')
        endData = ts.get_hist_data(str(code), start='2015-09-30', end='2015-09-30')
        # beginPrice = beginData['close'][0]
        # print(beginData)
        n_data.loc[sub] = [code, beginData['close'][0], endData['close'][0]]
        sub += 1
    except:
        pass

print(n_data)
n_data.to_excel('chajia.xlsx')
