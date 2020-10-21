# 综合 电子
import pandas as pd
start = '2020-01-01'
end = '2020-09-014'
benchmark = 'HS300'
universe = ['000425.XSHE']
capital_base = 100000
freq = 'd'
refresh_rate = 60
max_history_window = 60

def initialize(account):
    pass

def handle_data(account):
    hist = account.get_attribute_history('closePrice', 60)
    momentum = {'symbol': [], 'c_ret': []}
    for stk in hist.keys():
        momentum['symbol'].append(stk)
        momentum['c_ret'].append(hist[stk]['closePrice'][-1]/hist[stk]['closePrice'][0])
    momentum = pd.DataFrame(momentum).sort(columns='c_ret', ascending=False.reset_index())
    momentum = momentum[:60]
    buylist = momentum['symbol'].tolist()
    for stk in account.get_positions():
        if stk not in buylist:
            account.order_to(stk, 0)
    protfolio_value = account.portfolio_value
    for stk in buylist:
        account.order_pct_to(stk, 1.0/len(buylist))