import pickle
import pandas as pd
from scipy.stats import uniform, randint
# from category_encoders import OrdinalEncoder
from category_encoders import TargetEncoder
from xgboost import XGBRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import make_pipeline

if __name__ == '__main__':
    df = pd.read_csv('bicycle.csv')

    df.drop(columns = 'Unnamed: 0', inplace=True)

    target = '가격'
    feature = df.drop(columns = target).columns

    X = df[feature]
    y = df[target]

    pipe = make_pipeline(
        TargetEncoder(),
        XGBRegressor(random_state=2)
    )

    dists = {
        'targetencoder__smoothing': [2.,20.,50.,60.,100.,500.,1000.],
        'targetencoder__min_samples_leaf': randint(1, 10),
        'xgbregressor__n_estimators' : randint(5,200),
        'xgbregressor__max_depth' : randint(5,20),
        'xgbregressor__learning_rate' : uniform(0,1) 
    }

    xgb = RandomizedSearchCV(
        pipe,
        param_distributions= dists,
        scoring= 'r2',
        n_iter= 50,
        cv = 3,
        verbose = 1,
        n_jobs = -1,
        random_state = 2
    )

    xgb.fit(X,y)

    print(xgb.best_score_)
    model = xgb.best_estimator_

    with open('model_2.pkl', 'wb') as pickle_file:
        pickle.dump(model, pickle_file)