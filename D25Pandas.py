import pandas as pd
import numpy as np

# creating a series
names = ["Bob","Aaron", "Mike", "Jennifer", "Hailey"]
favorites = {"fruit":"strawberry","vegetable":"iceburg lettuce","sport":"running"}
list_series = pd.Series(names, index=[5,6,7,8,9]) # default index is 0 through number of items
dict_series = pd.Series(favorites)
const_series = pd.Series(5, index=[1,2,3])
linspace_series = pd.Series(np.linspace(0, 10, 5))
print(f"{list_series}\n{dict_series}\n{const_series}\n{linspace_series}")