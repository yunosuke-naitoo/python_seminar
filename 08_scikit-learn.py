from matplotlib import pyplot as plt
from sklearn import datasets

# bostonデータの読み込み
boston = datasets.load_boston()

# グラフのサイズ
plt.figure(figsize=(30, 8))

# 13項目分の散布図を作成
for i in range(13):
    # 2×7のグラフを作成
    plt.subplot(2, 7, i + 1)
    # 散布図の描画
    plt.scatter(
        # 列の全データ
        boston.data[:, i],
        # 住宅の価格
        boston.target,
        marker = 'o',
        c = 'b'
    )
    # bostonデータセットのカラム名
    plt.xlabel(boston.feature_names[i])
    plt.ylabel('house price')
    plt.autoscale()
    plt.grid()
plt.show()




# 平均部屋数(RM)が増えれば、住宅の価格は高くなると読み取った場合
# 平均部屋数(RM)と住宅の価格の最小二乗法を適応
import numpy as np

# 平均部屋数
rm = boston.data[:, 5]
# 住宅の価格
prices = boston.target

x = np.array([[v, 1] for v in rm])
y = prices
(slope, bias), total_error, _, _ = np.linalg.lstsq(x, y)

# グラフの描画
plt.figure(figsize=(30, 8))
plt.plot(x[:, 0], slope * x[:, 0] + bias)
plt.scatter(
    rm,
    prices,
    marker = 'o',
    c = 'b',
)
plt.xlabel(boston.feature_names[5])
plt.ylabel('house price')
plt.autoscale()
plt.grid()
plt.show()


import statsmodels.api as sm

# サンプル数
nsample = rm.size

#
X = np.column_stack((np.repeat(1, nsample), rm))

# 回帰実行
model = sm.OLS(prices, X)
results = model.fit()

# 結果のサマリを表示
print(results.summary())

# パラメータの推定値を取得
a, b = results.params

# プロット
plt.plot(rm, prices, 'o')
plt.plot(rm, a + b * rm)
plt.show()

