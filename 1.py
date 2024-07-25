import pandas as pd

titanic = pd.read_csv("titanic.csv")

# print(titanic)

titanic.head(8)

titanic.dtypes

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)