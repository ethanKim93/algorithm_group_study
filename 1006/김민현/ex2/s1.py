array = [i for i in range(1,11)]

for i in range(1<<10):
    ans = []
    for j in range(10):
        if i&(1<<j):
            ans.append(array[j])
            if sum(ans)>10:
                break
    if sum(ans) == 10:
        print(ans)