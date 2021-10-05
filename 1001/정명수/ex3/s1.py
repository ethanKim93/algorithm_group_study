num = [-1,3,-9,6,7,-6,1,5,4,-2]

n = len(num)
for i in range(1<<n):
    part = []
    for j in range(n):
        if i & (1 << j):
            part.append(num[j])
    if sum(part)==0:
        print(part)
