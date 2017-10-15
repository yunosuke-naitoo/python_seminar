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



