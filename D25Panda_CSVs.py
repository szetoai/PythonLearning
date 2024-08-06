import pandas as pd

# opening csv
df = pd.read_csv("D25REF_data.csv")
print(f"{df.head(10)}\n{df.tail(10)}\n{df.shape}\n{df.columns}") # first 10, last 10, shape, columns
print(df["Height"]) # print a series of one column
print(df["Height"].describe()) # data about column
print(df.describe()) # dataframe about dataframe
