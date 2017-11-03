# 辞書を作成
dic = {'Apple' : 'Red', 'Lemon' : 'Yellow'}

# インデックスアクセス
dic['Apple']

# in構文を使って辞書にキーが登録うされているか確認
'Apple' in dic
'Grape' in dic

# 辞書を追加
dic['Grape'] = 'Purple'

# 削除
del dic['Lemon']

# イテレーションアクセス
# 全てのキーを表示
for key in dic:
    print(key)
    
# valueを表示
for value in dic.values():
    print(value)

# keyとvalueを同時に表示
for key, value in dic.items():
    print(key, value)
