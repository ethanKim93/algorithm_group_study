arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def powerset(i ,N, k):
    if i == k:
        total = 0
        for l in range(k):
            total += arr[l]
        if total == 10:
            print(arr[:k])
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            powerset(i+1, N, k)
            arr[i], arr[j] = arr[j], arr[i]

for k in range(1, len(arr)+1):
    powerset(0, len(arr), k)