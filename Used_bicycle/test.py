import pickle
import numpy as np
import pandas as pd
from flask import request
import datetime

df =pd.read_csv('bicycle.csv')

print(df)