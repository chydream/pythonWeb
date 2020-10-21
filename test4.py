import datetime
import pandas as pd
import numpy as np

# pd.set_option('max_columns', 28, 'max_rows', 10)
movie = pd.read_csv('data/movie.csv')
movie1 = movie.select_dtypes(include=['number']).head()
movie2 = movie.filter(items=['actor_1_name', 'asdf']).head()
print(movie2)

