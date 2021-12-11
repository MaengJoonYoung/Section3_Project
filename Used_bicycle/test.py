import pandas as pd

df = pd.read_csv('/Users/maengbook/Desktop/Project_3/bicycle.csv')

print(df['brand'].unique())