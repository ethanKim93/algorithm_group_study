def powerset(idx, target):
    if idx == N:
        total = 0
        for i in range(N):
            if bit[i]:
                total += arr[i]
        if target == total:
            for i in range(N):
                if bit[i]:
                    print(arr[i], end=' ')
            print()
    else:
        bit[idx] = 1
        powerset(idx + 1, 10)
        bit[idx] = 0
        powerset(idx+1, 10)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
bit = [0] * N
powerset(0, 10)