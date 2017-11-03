# リストの作成
x = [1, 2, 3, 'a', 'b', 'c']
# インデックスを使ってアクセス
print(x[0])
print(x[3])
# リストの末尾からアクセスしたい場合
print(x[-1])
print(x[-2])

# スライス
# x[n:m] -> n番目か番目からm-1番目の要素を取り出す
x[1:2]
x[1:4]
x[4:]
x[:4]

# 要素の追加
x.append('d')
print(x)
# 要素の削除
x.remove('a')
print(x)

# リストのソート
y = [2, 3, 5 ,6, 1, 2]
y.sort()
y
# リストを逆順にする
y.reverse()
y

# 1行で降順にしたい場合
y.sort(reverse=True)

# タプルの作成
z = (1, 2, 3, 'a', 'b', 'c')
z[0]
z[1:4]
