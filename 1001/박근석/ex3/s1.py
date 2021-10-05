list_a = [-1,3,-9,6,7,-6,1,5,4,-2]
count = 0

for i in range(1<<len(list_a)):

    arr = []
    for j in range(len(list_a)):
        if i & (1<<j):
            arr.append(list_a[j])
    if sum(arr) == 0:
        count += 1

print(count-1)
