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
            rs = num1 / num2    
        rs = '計算エラー'
    return rs

print(calc(3, 0, 4))
