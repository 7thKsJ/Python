a = dict()
b = list(input().split())
for i in b:
    sstr1 = i.split(':')
    name = sstr1[0]
    pw1, pw2 = sstr1[1].split(',')
    sstr1[1] = pw1+' '+pw2
    a[sstr1[1]] = name;
_key = input()
if _key in a :
    print(a[_key])
else:
    print('Not Found!!')
