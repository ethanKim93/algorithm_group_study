def selection_sort(i, mn_idx, k):
    if i == n:
        maps[k], maps[mn_idx] = maps[mn_idx], maps[k]
        return

    if maps[mn_idx] > maps[i]:
        mn_idx = i

    selection_sort(i+1, mn_idx, k)

maps = [6,5,4,7,9,11,43,5]
n = len(maps)
for i in range(n-1):
    selection_sort(i,i,i)
print(maps)