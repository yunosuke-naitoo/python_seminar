import matplotlib.pyplot as plt
from numpy.random import randn
from ggplot import *

# 標準正規分布を生成
# cumsumで足していく
plt.plot(randn(100).cumsum())
plt.plot(randn(100).cumsum(), 'k--')

# オプションを明示的に指定
plt.plot(randn(30).cumsum(), color = 'k', linestyle='--', marker='o')


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five', ], rotation=30, fontsize='small')
ax.set_title('My first plot')
ax.set_xlabel('Stage')


# ggplot
meat.head()
ggplot(aes(x='date', y='beef'), data=meat) + \
geom_point(color='lightblue') + labs() + \
stat_smooth(span=.15, color='black', se=True)

