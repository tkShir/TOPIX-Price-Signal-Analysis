# 基本パッケージ（numpy,Pandas,matplotlib）
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 線形サポートベクターマシーン
from sklearn.svm import LinearSVC
# train_test_split（データを分割出してくれる）
from sklearn.model_selection import train_test_split
# accuracy_score（正解率を測れる）
from sklearn.metrics import accuracy_score
# グリッドサーチ（ハイパーパラメータを自動的に最適化してくれる）
from sklearn.model_selection import GridSearchCV
# 正規化
from sklearn.preprocessing import MinMaxScaler
# 交差検証
from sklearn.model_selection import cross_val_score
# warningの抑制
import warnings
# モデルの保存
from sklearn.externals import joblib

def ProcessDF():
    res_df = pd.read_csv("result.csv", header = 0)

    #separating answer variables and dropping date column
    answers = res_df.Answer.values
    res_df.drop(columns=['Answer'], inplace=True)
    res_df.drop(columns=['Date'], inplace=True)

    #fill nan with average of each column
    res_df = res_df.fillna(res_df.mean())

    #conver df to np array
    explanatory_variable = res_df.values

    #scaling
    ms = MinMaxScaler()
    ms.fit(explanatory_variable)
    explanatory_variable = ms.transform(explanatory_variable)

    #split train and test data
    X_train, X_test, y_train, y_test = train_test_split(explanatory_variable , answers, test_size=0.2, random_state=1,shuffle = False)

    # Set grid search parameters
    parameters = {'C':[0.01,0.1,1,10,100],'loss':['hinge', 'squared_hinge']}
    # Grid Searching
    lsvc =  LinearSVC(random_state=1)
    grid_search = GridSearchCV(lsvc, param_grid=parameters, cv=5)
    grid_search = grid_search.fit(X_train , y_train)

    # Result of Grid Search
    GS_C, GS_loss = grid_search.best_params_.values()
    print ("Appropriate Parameter {}".format(grid_search.best_params_))

    # Calculate most appropriate parameters
    clf = LinearSVC(loss=GS_loss, C=GS_C, random_state=1)
    clf.fit(X_train , y_train)

    # Post-training testing
    # Predict using the training data
    y_train_pred = clf.predict(X_train)
    # Predict using the test data
    y_val_pred = clf.predict(X_test)

    # Calculate the accuracy_score for train and test datas
    train_score = accuracy_score(y_train, y_train_pred)
    test_score = accuracy_score(y_test, y_val_pred)
    # Display accuracy
    print("Accuracy with Training Data：" + str(train_score * 100) + "%")
    print("Accuract with Test Data" + str(test_score * 100) + "%")

    # Cross validation
    # Split into 5 sections for cross validations
    scores = cross_val_score(clf, explanatory_variable, answers, cv=5)
    # Score of indvidual sections
    print('Cross-Validation scores: {}'.format(scores))
    # Average score
    print('Average score: {}'.format(np.mean(scores)))

ProcessDF()
