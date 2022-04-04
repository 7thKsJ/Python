a = input().split()
b = a
max = 0
maxstr = ''
b = list(set(b))
for i in b:
    if a.count(i) > max:
        max = a.count(i)
        maxstr = i
print(int(maxstr),max)
