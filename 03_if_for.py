###################### 条件分岐 ######################

# テストの点数
point = 39

if point >= 80 :
    print('良い')
elif point >= 40 and point < 80 :
    print('普通')
else :
    print('悪い')


###################### 繰り返し ######################

points = [90, 20, 45, 78, 100]

for i in points :
    print(i)


points = {'naito' : 90, 'yamada' : 80, 'tanaka' : 100}
for name, point in points.items() :
    print(name+'さんの点数は'+str(point)+'点です')

# 処理の後に実行する場合はelseをつける    
for i in range(10):
    print(i)
else:
    print("end")

# 文字列を1文字ずつ表示する
for str in "Hello!!":
    print(str)

# 10回ループしたら処理を停止する
for i in range(20):
    if i == 10:
        break
    print(i)
    
# continueで処理をスキップできる
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
