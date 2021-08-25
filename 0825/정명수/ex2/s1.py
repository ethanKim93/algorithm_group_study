chew = 20
number = [1]*10 # 9명 있다고 가정
i = 1
q = []
while chew > 0:
    a = input()
    q.append(i)
    k = q.pop(0)
    q.append(k)
    chew -= number[k]
    print(len(q))
    print(number[k])
    print(20-chew)
    number[k] += 1
    i += 1
print(k)




