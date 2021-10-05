A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(A)
ans = 0
for i in range(1, 2 ** 10):
    tot = 0
    result = []
    for j in range(10):
        if i & (1 << j):
            tot += A[j]
            result += [A[j]]
    if not tot:
        print(result)
        ans += 1
print('{}개 존재'.format(ans))