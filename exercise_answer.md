### 問題1
```{python}
for i in range(1, 11):
    if i % 2 == 0:
        print('%dは偶数です' % i)
    else:
        print('%dは奇数です' % i)
```

### 問題2

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
