from pandas import Series, DataFrame
import pandas as pd

### SeriesとDataFrame

## Series
'''
シリーズは１次元の配列のようなオブジェクトで
'''
obj = Series([3, 6, 13, 4])
obj
'''
左側がインデックス
右側がデータ
'''

# データ表示
obj.values
# インデックス表示
obj.index

# インデックス付きのシリーズを作成
obj2 = Series([2, 4, 7, 1], index=['a', 'b', 'c', 'd'])
obj2
# インデックス表示
obj2.index

obj2['a']
obj2[obj2>3]
obj2 * 2 

# オブジェクトに指定のインデックスが存在するか
'a' in obj2
'k' in obj2

# ディクショナリ形式のデータを使ってシリーズを作成
data = {'neko' : 100, 'inu' : 390, 'saru' : 30}
obj3 = Series(data)
obj3

states = ['neko', 'inu', 'uma']
obj4 = Series(data, states)
obj4

# NaNは欠損値
obj4.isnull()
obj4.notnull()

# インデックスに名前をつける
obj4.index.name = 'animal'
obj4




## DataFrame
'''
データフレームはテーブル形式のスプレットシート風のデータ構造を持ち、順序付けられた
列を持っている。

作成したデータフレームには自動的にインデックスがつけられる
'''

data = {'name' : ['tanaka', 'sato', 'naito', 'yamada'],
        'sex' : ['male', 'female', 'male', 'male'],
        'height' : [190, 160, 168, 174]}
frame = DataFrame(data)
frame

# 列の順番を指定して作成
frame = DataFrame(data, columns=['name', 'sex', 'height'])
frame

# Series同様、指定した列がデータを持たない場合はNaNと表示される
frame2 = DataFrame(data, columns=['name', 'sex', 'height', 'age'])
frame2
# 列の一覧を取得
frame2.columns

# 身長だけを抽出
frame2['height']
frame2.height

# インデックスを参照して行を抽出
frame2.ix[0]

# age列にでデータを追加
frame2['age'] = Series([20, 30, 30, 41], index=[0, 1, 2, 3])
frame2

frame2['hantei'] = frame2.height >= 170

frame2['displayName'] = Series(['田中', '佐藤', '内藤', '山田'])
frame2

# 行の削除
frame2.drop(3)

# 列の削除
del frame2['hantei']
frame2

# 条件で検索
frame2[frame2.age >= 30]


## Seriesの算術
s1 = Series([23, 4, 5.6, 21], index=['a', 'b', 'c', 'd'])
s2 = Series([90, 24, 9.1, 100], index=['c', 'd', 'e', 'f'])

s1
s2
# 重複していないインデックスではNA値が割り当てられる
s1 + s2


df1 = DataFrame(np.arange(9).reshape((3, 3)), columns=list('abc'))
df2 = DataFrame(np.arange(9).reshape((3, 3)), columns=list('cde'))

df1
df2

df1 + df2


df1.add(df2, fill_value=0)


## ソート
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
# インデックスでソート
obj.sort_index()

frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
frame.sort_index()
frame.sort_index(axis=1)

# 降順でソート
frame.sort_index(axis=1, ascending=False)

# 列を指定してソート
frame = DataFrame({'a' : [1, 5, 4, 3, 8], 'b' : [9, 2, 3, 6, 8]})
frame.sort_index(by='b')


## 要約統計量 p157
df = DataFrame([[2, np.nan], [7, 6], [np.nan, np.nan], [-2, 9]], columns=['a', 'b'])
df
# 列の合計(NAは無視される)
df.sum()
# 行で合計
df.sum(axis=1)
# 平均
df.mean()
# 累積
df.cumsum()

# 要約統計量をまとめて表示
df.describe()

## 欠損値の取り扱い
string_data = Series(['aaa', 'bbb', np.nan, 'ddd'])
string_data
string_data.isnull()

# 欠損値を除外する
from numpy import nan as NA
string_data.dropna()

# データフレームの場合
df = DataFrame([[1, 2, 3], [3, NA, NA], [NA, NA, NA], [NA, 9, 8]])
df
# dropnaメソッドはデフォルトで欠損値を含む行（列）を削除する
df.dropna()
# how='all'を指定することで全てのデータがNAのぎ行を削除する
df.dropna(how='all')
df[4] = NA
df
df.dropna(axis=1, how='all')

# 欠損値の穴埋め
df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
df
# NAを0で穴埋め
df.fillna(0)
df.fillna({1: 0.5, 2: 0})
