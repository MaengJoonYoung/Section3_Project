import sqlite3
import pickle

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

# add_data('data_2.pkl')

conn.commit()
conn.close()