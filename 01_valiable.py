# 文字列
a = 'Python'

# 数値
b = 100

# 標準出力
print(a)
print(b)

# 型の調べ方
print(type(a))
print(type(b))

# 文字列の結合
str1 = 'Python'
str2 = '入門'
str3 = str1 + str2
print(str3)


# コンソールからの入力値を受け取る
print('名前を教えてください')
name = raw_input()
print('年齢は？')
age = raw_input()
print('こんにちは%s(%s歳)さん' % (name, age))
