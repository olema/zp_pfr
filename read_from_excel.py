import pandas as pd

df = pd.read_excel("Forma_.xlsx", sheet_name="Раздел 1")
print(df)
print("\n\n=========================\n\n")
print(df.info())
print("\n\n=========================\n\n")
print(df
