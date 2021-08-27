#마이쭈

n = 20 #마이쮸 갯수
q = [1]
p = []
while n>0:
    p.append(1)
    temp = q.pop(0)
    n -= p[temp - 1]
    p[temp-1] += 1
    q.append(temp)
    q.append(len(p)+1)
print(temp)
input()
print(len(q)-1)
input()
for i in range(1,len(q)):
    print('{}번 {}개'.format(i,p[i-1]))
input()
print(sum(p))

