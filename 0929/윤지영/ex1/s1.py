li = input()
num = [[] for _ in range(len(li)//7)]
j = 0
for i in range(0,len(li)-6,7):
    num[j]=li[i:i+7]
    j+=1

for k in range(len(num)):
    l = len(num[k])
    result = s = 0
    for m in range(l-1,-1,-1):
        result += (1 << s) * int(num[k][m])
        s += 1
    print(result, end=' ')

