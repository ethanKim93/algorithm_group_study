#마이쭈

n = 20 #마이쮸 갯수
q = [1]
p = []
i = 0
while n>0:
    p.append(1)
    temp = q.pop(0)
    n -= p[temp - 1]
    p[temp-1] += 1
    q.append(temp)
    if n == 0:
        break
    q.append(len(p)+1)
    if n == 0:
        break
    a = 1
print(temp)

