from flask import Flask, render_template
import pandas as pd

df =pd.read_csv('/Users/maengbook/Desktop/Project_3/bicycle.csv')


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        brand_list = df['brand'].unique()
        drivetrain_list = df['drivetrain'].unique()
        material_list = df['material'].unique()
        return render_template('home.html', brand_list= brand_list, drivetrain_list = drivetrain_list, material_list = material_list)
    
    return app