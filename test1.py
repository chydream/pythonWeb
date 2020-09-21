import pandas as pd
start = '2020-01-01'
end = '2020-09-13'
benchmark = 'HS300'
universe = DynamicUniverse('HS300')
refresh_rate = 60
max_history_window = 60
accounts = {
    'fantasy_account':AccountConfig(account_type='security', capital_base=10000000, commission=Commission(buycost=0.001, sellcost=0.002, unit='perValue'),slippage=Slippage(value=0.0, unit='perValue'))
}

def initialize(context):
    pass

def handle_data(context):
    account = context.get_account('fantasy_account')
    universe = context.get_universe(exclude_halt=True)
    history = context.history(universe, 'closePrice', 60)
    momentum = {'symbol': [], 'c_ret':[]}
    for stk in history.keys():
        momentum['symbol'].append(stk)
        momentum['c_ret'].append(history[stk]['closePrice'][-1]/history[stk]['closePrice'][0])
    momentum = pd.DataFrame(momentum).sort(columns='c_ret', ascending=False).reset_index()
    momentum = momentum[:60]
    buylist = momentum['symbol'].tolist()
    for stk in account.get_positions():
        if stk not in buylist:
            account.order_to(stk, 0)
    protfolio_value = account.portfolio_value
    for stk in buylist:
        account.order_pct_to(stk, 1.0/len(buylist))

