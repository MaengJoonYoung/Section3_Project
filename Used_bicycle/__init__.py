from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

df =pd.read_csv('/Users/maengbook/Desktop/Project_3/bicycle.csv')

app = Flask(__name__)

@app.route('/')
def home():
    brand_list = df['brand'].unique()
    drivetrain_list = df['drivetrain'].unique()
    material_list = df['material'].unique()
    return render_template('home.html', brand_list= brand_list, drivetrain_list = drivetrain_list, material_list = material_list)
    
@app.route('/predict/', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        brand = request.form.get('brand')
        old = request.form.get('old', type=int)
        brake = request.form.get('brake')
        drivetrain = request.form.get('drivetrain')
        material = request.form.get('material')
        
        pred_df = pd.DataFrame({'brand' : [brand], 'old': [old], 'brake' : [brake], 'drivetrain': [drivetrain], 'material': [material]})
            
        predcit_price = int(model.predict(pred_df))

        return render_template('predict.html', predcit_price = predcit_price)

if __name__ == '__main__':
    model = None
    with open('model_2.pkl', 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    app.run()