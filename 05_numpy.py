import numpy as np

# 配列定義
arr = np.array([[1, 2, 3], [11, 12, 13]])
print(arr)

# 配列のでデータ型を確認
arr.dtype

arr2 = np.array([1, 2, 3, 4, 5])
# インデックスでアクセス
print(arr2[0])
# スライス
print(arr2[0:2])

# イテレーション
for i in arr2:
    print(i)


# 配列の計算
# 配列に定数をかける
print(arr2 * 2)

# 配列同士を足す
arr3 = np.array([11, 12, 13, 14, 15])
print(arr2 + arr3)

# 配列の内積
arr2.dot(arr3)

# 配列の形を見る
arr2.shape

# 平均
arr2.mean()

# 最大値と最小値
arr2.min()
arr2.max()

# 合計
arr2.sum()

# 標準偏差
arr2.std()

# 多次元配列
a = np.array([[1, 2, 3, 4], [11, 12, 13, 14]])
np.mean(a, axis=0)
np.mean(a, axis=1)

# 配列の中身を検索(条件にマッチするインデックスを取得)
arr4 = np.array([3, 6, 8, 10])
np.where(arr4 > 1)
arr4[np.where(arr4 > 2)]

np.where(arr4 == 6, 'roku', 'rokudehanai')



