from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from prepare_data import X, Y
import matplotlib.pyplot as plt
from joblib import dump, load
from pprint import pprint
import numpy as np
import pandas as pd



def evaluate_model(model):
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    R2.append(r2_score(Y_test, Y_pred))
    MAE.append(mean_absolute_error(Y_test, Y_pred))
    MSE.append(mean_squared_error(Y_test, Y_pred))

    Y_pred = scaler_y.inverse_transform(Y_pred.reshape(-1, 1))
    data[model] = Y_pred.flatten()
    # scores = cross_validate(model, X, Y, scoring=['r2', 'neg_mean_absolute_error', 'neg_mean_squared_error'])
    #
    # R2.append(scores['test_r2'].mean())
    # MAE.append(scores['test_neg_mean_absolute_error'].mean())
    # MSE.append(scores['test_neg_mean_squared_error'].mean())

scaler_x = load('scaler_x.joblib')
scaler_y = load('scaler_y.joblib')
MODELS = [DecisionTreeRegressor(), RandomForestRegressor(), SVR(), KNeighborsRegressor()]
R2 = []
MAE = []
MSE = []
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
data = {
    'Angle': scaler_y.inverse_transform(Y_test.reshape(-1, 1)).flatten(),
    MODELS[0]: [],
    MODELS[1]: [],
    MODELS[2]: [],
    MODELS[3]: [],
}


for model in MODELS:
    evaluate_model(model)

# X_axis = np.arange(len(MODELS))
#
# plt.figure(figsize=(13,11))
# plt.bar(X_axis-0.3, R2, 0.3, label = 'R Square', color='royalblue')
# plt.bar(X_axis, np.dot(MAE, -1), 0.3, label = 'MAE', color='magenta')
# plt.bar(X_axis+0.3, np.dot(MSE, -1), 0.3, label = 'MSE', color='deepskyblue')
# plt.xticks(X_axis, MODELS)
# plt.legend()
# plt.savefig('model_results.png')



pprint(data)

df = pd.DataFrame(data)

print(df)
# pd.set_option('display.max_columns', 5)

