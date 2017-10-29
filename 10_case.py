import pandas as pd

# カンマ区切りのデータを読み込む
names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
names1880

# 性別ごとの出生数
names1880.groupby('sex').births.sum()

# 全てのファイルを読み込む
years = range(1880, 2017)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    # ファイルパス
    path = 'names/yob%d.txt' % year
    # ファイルの読み込み
    frame = pd.read_csv(path, names=columns)
    # 年のカラムを追加
    frame['year'] = year
    pieces.append(frame)
# piecesに格納された要素を一つのデータフレームにまとめる
names = pd.concat(pieces, ignore_index=True)
names

# 年度ごとの男女別出生数
total_birth = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
total_birth.plot(title='total births by sex and year')

# 全出生数に対するその名前の割合を求める。年度別・性別ごとに計算
def add_prop(group):
    # intger同士の除算は切り上げされてしまうためfloatにキャスト
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)
names

# 年代・性別ごとの上位1000件の名前がどのようなものであるかを見てみる
def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000

# 名前の傾向分析
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

# top1000を年代別のデータとして整理する
total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
# John, Harry, Maryを選んでみる
subset = total_births[['John', 'Harry', 'Mary']]
subset.plot(subplots=True)

# 子供の名前をつけるとき、一般的な名前を選ばない傾向があるのではないか。という仮説たb
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))



