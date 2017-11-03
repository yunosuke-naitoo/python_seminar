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

# 子供の名前をつけるとき、一般的な名前を選ばない傾向があるのではないか。という仮説
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
table.plot(yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# 名付けの多様性が年を経るごとに増加している


# 出生数の半分(50%)が、何種類の名前で構成されているのか、例として2010年の男性のデータを見る
df = boys[boys.year == 2010]
df

# 割合を降順にソートして累積を求める
prop_cumsum = df.sort_index(by='prop', ascending=False).prop.cumsum()
prop_cumsum[:10]
# 要素の値に近いインデックスを返す
prop_cumsum.searchsorted(0.5)

df = boys[boys.year == 1900]
in1900 = df.sort_index(by='prop', ascending=False).prop.cumsum()
in1900.searchsorted(0.5) + 1

# 前年度に対して実行
# groupごとに50%点を返す関数を作成
def get_quantile_count(group, q = 0.5):
    group = group.sort_index(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1

# 年・性別ごとに分類し、そのgroupごとの50%点を取得
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# 性別を列に持ってくる
diversity = diversity.unstack('sex')
diversity = diversity.astype(float)
diversity.plot()

# 名前の付け方の多様化に伴う、末尾文字の変化
# 末尾文字を抽出する無名関数lambdaを作成
get_last_letter = lambda x: x[-1]
# Series.mapの引数に関数を与えると、要素一つ一つに関数を適応してくれる
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

# 横軸にa~zまで26文字分の26行、縦軸に1880年lから2016年までの男女別の表
table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)

# サンプルとして、1910年,1960年,2010年を代表として見てみる
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
subtable.head()

# この集計表では年度間の比較に適さないので、各年度の全出生数で割る
letter_prop = subtable / subtable.sum().astype(float)

# 棒グラフを使って比較
letter_prop['M'].plot(kind='bar')
letter_prop['F'].plot(kind='bar')

# 前年度に対して男性のd, n, yに着目してみる
letter_prop = table / table.sum().astype(float)
dny = letter_prop.ix[['d', 'n', 'y'], 'M'].T
dny.plot()
