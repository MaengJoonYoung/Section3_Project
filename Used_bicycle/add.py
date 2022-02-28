import sqlite3
import pickle
import pandas as pd
conn = sqlite3.connect('used_bicycle.db')
cur = conn.cursor()

def init_db():
    cur.execute("DROP TABLE IF EXISTS bicycle")
    cur.execute("""
    CREATE TABLE bicycle(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand VARCHAR,
        price VARCHAR,
        old INTEGER,
        brake VARCHAR,
        drivetrain VARCHAR,
        material VARCHAR
    );""")

# 부호화 한 데이터를 데이터베이스에 입력.
def add_data(data):

    datas = None

    with open(data, 'rb') as pickle_file:
        datas = pickle.load(pickle_file)

    for data in datas:
        try:
            if len(data) >= 8 :
                cur.execute("INSERT INTO bicycle (brand, price, old, brake, drivetrain, material) VALUES (?,?,?,?,?,?);", 
                (data['브랜드'], data['가격'], int(data['연식']), data['브레이크'], data['구동계'], data['소재']))
        except:
            pass

# 전처리 후 bicycle_pre라는 테이블 이름으로 데이터베이스에 데이터 적재.
def after_preprocessing(df):
    df['price'] = df['price'].replace({',' : '', '원' : ''})
    con = sqlite3.connect('used_bicycle.db')
    df.to_sql('bicycle_pre', con, index=False)

# 코랩에서 전처리를 진행했던 csv 파일을 데이터베이스에 적재.
df = pd.read_csv('bicycle.csv')
# init_db()
# add_data('data.pkl')
# add_data('data_2.pkl')
after_preprocessing(df)
conn.commit()
conn.close()