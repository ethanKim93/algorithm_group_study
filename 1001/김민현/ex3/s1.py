arr = [-1,3,-9,6,7,-6,1,5,4,-2]


n = len(arr)

for i in range(0,(1<<n)):
    part = []
    for j in range(0,n):
        if i & (1<<j):
            part.append(arr[j])
    if sum(part) == 0:
        print(part)

