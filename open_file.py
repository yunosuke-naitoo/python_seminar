import codecs

# ファイルの内容を一括で表示
f = codecs.open('hello.txt')
print(f.read())
f.close()

# 1行ずつ表示
f = codecs.open(filename='hello.txt', mode='r', encoding='utf-8')
for line in f:
    print(line.replace('\n', ''))
f.close()

# 出現回数を数える
f = codecs.open('hello.txt')
search = raw_input()
count = 0
for line in f:
    if line.find(search) == 0:
        count += 1
print(count)
f.close()


