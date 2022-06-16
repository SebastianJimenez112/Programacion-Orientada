import pandas as pd

miData=pd.read_csv("Predio.csv", nrows=100)
print(miData.head())
print(miData["PRENBARRIO"])
row=miData.iloc[1]
print(row)
print(miData.shape)

