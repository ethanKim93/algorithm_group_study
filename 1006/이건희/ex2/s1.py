alist = [1,2,3,4,5,6,7,8,9,10]

n = len(alist)
ans = []
for i in range(1<<n):
    temps = []
    sm = 0
    flag = False
    for x in range(i):
        if i & (1<<x):
            temps.append(alist[x])
            sm += alist[x]
            if sm > 10:
                flag = True
                break

    if not flag:
        if sm == 10:
            ans.append(temps)

print(ans)

# Pass