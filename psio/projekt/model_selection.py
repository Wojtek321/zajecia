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
    model.fit(X_train, np.ravel(Y_train))
    Y_pred = model.predict(X_test)

    R2.append(r2_score(Y_test, Y_pred))
    MAE.append(mean_absolute_error(Y_test, Y_pred))
    MSE.append(mean_squared_error(Y_test, Y_pred))

    Y_pred = scaler_y.inverse_transform(Y_pred.reshape(-1, 1))
    data[model] = Y_pred.flatten()


scaler_x = load('scaler_x.joblib')
scaler_y = load('scaler_y.joblib')
MODELS = [DecisionTreeRegressor(max_depth=5,max_leaf_nodes=26,min_samples_split=8), RandomForestRegressor(min_samples_split=4,n_estimators=4), SVR(), KNeighborsRegressor()]
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


X_axis = np.arange(len(MODELS))

plt.figure(figsize=(13,11))
plt.bar(X_axis-0.3, R2, 0.3, label = 'R Square', color='royalblue')
plt.bar(X_axis,MAE, 0.3, label = 'MAE', color='magenta')
plt.bar(X_axis+0.3,MSE, 0.3, label = 'MSE', color='deepskyblue')
plt.xticks(X_axis, MODELS)
plt.legend()
plt.savefig('model_results.png')


df = pd.DataFrame(data)
df.to_excel('models_results.xlsx',index=False)
print(df.columns)


