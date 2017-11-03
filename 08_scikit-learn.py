from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
iris = load_iris()

iris.keys()
# 予測しようとしている花の種類
iris['target_names']
# 特徴量について
iris['feature_names']


# 訓練データとテストデータに分ける
## train_test_split
# データを並べ替えて、75%を訓練データに、残りの25%を訓練データに分割してくれる
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    iris['data'], iris['target'], random_state=0)

# 訓練データ
X_train.shape
y_train.shape

# テストデータ
X_test.shape
y_test.shape

# X_trainデータからデータフレームを作成
iris_df = pd.DataFrame(X_train, columns=iris.feature_names)
# データの観察
pd.scatter_matrix(iris_df, c=y_train, hist_kwds={'bins':20})

# k-最近傍法
from sklearn.neighbors import KNeighborsClassifier
# 今回は近傍点の数を1でやってみる
knn = KNeighborsClassifier(n_neighbors=1)
# モデル構築するにはfitメソッドを使うだけ.Numpy配列を使うこと
knn.fit(X_train, y_train)


# 予測してみる。以下のような野生のアイリスを見つけたとして、、、
# ガクの長さ：5cm
# ガクの幅　：2.9cm
# 花弁の長さ：1cm
# 花弁の幅　：0.2cm
X_new = np.array([[5, 2.9, 1, 0.2]])
X_new

prediction = knn.predict(X_new)
prediction
iris['target_names'][prediction] # setosaと分類された

# この分類結果が正しいのかどうかがわからないため、モデルの評価を行う
# scoreメソッドで精度を計算してくれる
knn.score(X_test, y_test)
