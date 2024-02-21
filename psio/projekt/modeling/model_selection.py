from data.prepare_data import X_train, X_test, Y_train, Y_test
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy as np


def evaluate_model(model):
    model.fit(X_train, np.ravel(Y_train))
    Y_pred = model.predict(X_test)

    R2.append(r2_score(Y_test, Y_pred))
    MAE.append(mean_absolute_error(Y_test, Y_pred))
    MSE.append(mean_squared_error(Y_test, Y_pred))


MODELS = [DecisionTreeRegressor(), RandomForestRegressor(), SVR(), KNeighborsRegressor()]
R2 = []
MAE = []
MSE = []

for model in MODELS:
    evaluate_model(model)


X_axis = np.arange(len(MODELS))
plt.clf()
plt.figure(figsize=(10, 8))
plt.title('Comparison of model performance metrics')
plt.bar(X_axis-0.3, R2, 0.3, label = 'R Square', color='royalblue')
plt.bar(X_axis, MAE, 0.3, label = 'MAE', color='magenta')
plt.bar(X_axis+0.3, MSE, 0.3, label = 'MSE', color='deepskyblue')
plt.xticks(X_axis, MODELS)
plt.legend()
plt.show()
