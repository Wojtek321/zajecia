from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from pprint import pprint
from model_selection import X_train, Y_train
from sklearn.model_selection import GridSearchCV
from statistics import mean
import numpy as np

dt = DecisionTreeRegressor()
rf = RandomForestRegressor()

rf_params = [{
    'n_estimators': [1, 2, 3, 4, 5, 6, 7, 8, 16, 32, 64, 100, 200],
    'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'min_samples_leaf': [1, 2, 4],
    }]

dt_params = [{
    'min_samples_split': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'max_depth': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
    'max_leaf_nodes': [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 26],
    }]

n_estimators_train = []
min_samples_split_train = []
min_samples_leaf_train = []

for i in range(0,5):
    grid_search = GridSearchCV(estimator=rf, param_grid=rf_params, n_jobs = -1)
    grid_search.fit(X_train,np.ravel(Y_train))
    params = grid_search.best_params_
    n_estimators_train.append(params['n_estimators'])
    min_samples_split_train.append(params['min_samples_split'])
    min_samples_leaf_train.append(params['min_samples_leaf'])

rf_n_estimators = mean(n_estimators_train)
rf_min_samples_split = mean(min_samples_split_train)
rf_min_samples_leaf = mean(min_samples_leaf_train)

pprint(n_estimators_train)
pprint(min_samples_split_train)
pprint(min_samples_leaf_train)

print('n_estimators', rf_n_estimators)
print('min_samples_split', rf_min_samples_split)
print('min_samples_leaf', rf_min_samples_leaf)

min_samples_split_train = []
max_depth_train = []
max_leaf_nodes_train = []

for i in range(0,5):
    grid_search = GridSearchCV(estimator=dt, param_grid=dt_params, n_jobs = -1)
    grid_search.fit(X_train,np.ravel(Y_train))
    params = grid_search.best_params_
    min_samples_split_train.append(params['min_samples_split'])
    max_leaf_nodes_train.append(params['max_leaf_nodes'])
    max_depth_train.append(params['max_depth'])

dt_min_samples_split = mean(min_samples_split_train)
dt_max_leaf_nodes = mean(max_leaf_nodes_train)
dt_max_depth = mean(max_depth_train)

pprint(min_samples_split_train)
pprint(max_leaf_nodes_train)
pprint(max_depth_train)

print('min_samples_split', dt_min_samples_split)
print('max_leaf_nodes', dt_max_leaf_nodes)
print('max_depth', dt_max_depth)


# grid_search = GridSearchCV(estimator=MODELS[0], param_grid=dt_params, n_jobs = -1)
# grid_search.fit(X_train,Y_train)
# pprint(grid_search.best_params_)

