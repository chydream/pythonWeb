import datetime
import pandas as pd
import numpy as np
dic = {
    'A': ['one', 'one', 'two', 'three'] * 6,
    'B': ['A', 'B', 'C'] * 8,
    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
    'D': np.random.randn(24),
    'E': np.random.randn(24),
    'F': [datetime.datetime(2013, i, 1) for i in range(1, 13)] + [datetime.datetime(2013, i, 15) for i in range(1, 13)]
}
df = pd.DataFrame(dic)
pt = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
pt1 = pd.pivot_table(df, values='D', index=['B'], columns=['A', 'C'], aggfunc=np.sum)
# print(df)
# print(pt)
# print(pt1)
tuples = list(zip(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print(df)
df2 = df[:4]
stacked = df2.stack()
print(stacked)
print(stacked.unstack(1))