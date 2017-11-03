### 問題1
```{python}
for i in range(1, 11):
    if i % 2 == 0:
        print('%dは偶数です' % i)
    else:
        print('%dは奇数です' % i)
```

### 問題2
```{python}
# 計算関数
# 第3引数には1~4の数値を入れる
# 1 : 足し算
# 2 : 引き算
# 3 : 掛け算
# 4 : 割り算
def calc(num1, num2, ope):
    if ope == 1:
        rs = num1 + num2
    elif ope == 2:
        rs = num1 - num2
    elif ope == 3:
        rs = num1 * num2
    elif ope == 4:
        if num2 != 0:
            rs = float(num1) / num2    
        else:
            rs = '計算エラー'
    return rs

print(calc(3, 0, 4))
```

### 問題3
```{python}
def BMI(height, weight):
    # メートルに変換
    height = float(height) / 100
    # BMIの計算
    bmi = float(weight) / (height * height)
    print bmi
    if bmi < 18.5:
        print('あなたのBMI指数は%sで、痩せぎみです' % bmi)
    elif bmi >= 18.5 and bmi < 25:
        print('あなたのBMI指数は%sで、標準体重です' % bmi)
    else:
        print('あなたのBMI指数は%sで、肥満体型です' % bmi)

print('あなたの身長は？')
height = raw_input()
print('あなたの体重は？')
weight = raw_input()

BMI(height, weight)
```
