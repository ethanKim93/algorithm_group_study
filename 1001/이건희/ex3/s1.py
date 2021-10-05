alist = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(alist)
for i in range(1<<n):
    temps = []
    for x in range(n):
        if i & (1 << x):
            temps.append(alist[x])
    if temps != [] and sum(temps) == 0:
        print(temps)