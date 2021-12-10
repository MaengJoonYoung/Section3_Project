import sqlite3
import pandas as pd

conn = sqlite3.connect('used_bicycle.db')

df = pd.read_sql_query("SELECT * FROM bicycle", conn)

print(df['brand'].value_counts())