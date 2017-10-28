import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()
# add_subplotでグラフを描画する領域を作成(2*2)
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# プロットすると一番最後のサブプロットに描画される
plt.plot(randn(50).cumsum(), 'k--')
# サブプロットを指定してプロットする
ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))


fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
       axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.3)
plt.subplots_adjust(wspace=0, hspace=0)


# 凡例つきグラフ
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(500).cumsum(), 'k', label='one')
ax.plot(randn(500).cumsum(), 'g--', label='two')
ax.plot(randn(500).cumsum(), 'r.', label='three')
ax.legend()

# pandasでも高度なプロットが出来る
from pandas import DataFrame
from pandas import Series
df = DataFrame(randn(10, 4).cumsum(0), columns=['A', 'N', 'C', 'D'], index=np.arange(0, 100, 10))
df.plot()

# 縦棒グラフと横棒グラフ
fig, axes = plt.subplots(2, 1)
data = Series(np.random.rand(16), index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0], color='k', alpha=0.4)
data.plot(kind='barh', ax=axes[1], color='g', alpha=0.4)

# 棒グラフのグループ化
df = DataFrame(np.random.rand(6, 4), 
            index=['one', 'two', 'three', 'four', 'five', 'six'], 
            columns=pd.Index(['A', 'B', 'C', 'D'], name='sample'))
df.plot(kind='bar')
# 積み上げ棒グラフ
df.plot(kind='bar', stacked=True, alpha=0.5)
