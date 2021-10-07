a = [1,2,3,4,5,6,7,8,9,10]

for i in range(1<<len(a)):
    arr = []
    for j in range(len(a)):
        if i & (1<<j):
            arr.append(a[j])
            if sum(arr) > 10:
                break
    if sum(arr) == 10:
        print(arr)
