import baostock as bs
import pandas as pd
import numpy as np
lg = bs.login()

# rs = bs.query_profit_data(code="sz.000639", year=2020, quarter=2)
# rs = bs.query_growth_data(code="sz.000639", year=2020, quarter=2)
# rs = bs.query_operation_data(code="sz.000639", year=2020, quarter=1)
# rs = bs.query_performance_express_report("sz.000639", start_date="2010-01-01", end_date="2020-12-31")
# rs = bs.query_performance_express_report("sh.600000", start_date="2020-01-01", end_date="2020-12-31")
# rs = bs.query_forecast_report("sz.000639", start_date="2010-01-01", end_date="2020-12-31")

# rs = bs.query_stock_basic(code="sh.600000")
rs = bs.query_stock_industry()
# rs = bs.query_sz50_stocks()
# rs = bs.query_history_k_data_plus('sh.000001',
#                                   'date, open, close, volume, turn, pctChg',
#                                   start_date='2020-08-01',
#                                   end_date='2020-08-03',
#                                   frequency='d', adjustflag='3')
# rs = bs.query_history_k_data_plus("sh.600000",
#     "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
#     start_date='2017-06-01', end_date='2017-12-31',
#     frequency="d", adjustflag="3")
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())

result = pd.DataFrame(data_list, columns=rs.fields)
# result1 = pd.DataFrame(result['industry'])
# result1['count'] = pd.Series(np.random.randint(1, 2, 4061))
# print(result1.groupby('industry').sum())
# result.to_csv('result.csv')
print(result)
bs.logout()