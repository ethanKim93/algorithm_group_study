arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
ls = []
ans = []
for i in range(1 << n):
    ls = []
    for j in range(n):
        if i & (1 << j):
            ls.append(arr[j])
        if not sum(ls):
            if ls not in ans and ls:    # 공집합 제거 / 중복 제거
                ans.append(ls)
print(ans)