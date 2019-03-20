import numpy as np
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
