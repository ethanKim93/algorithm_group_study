def gravity(arr):
    for c in range(9):
        for r in range(10):
            if arr[r][c] == 0:
                for row_idx in range(r - 1,- 1, -1):
                    arr[row_idx + 1][c] = arr[row_idx][c]
                    arr[row_idx][c] = 0
    return

arr = [list(map(int,input().split())) for _ in range(10)]
gravity(arr)
for i in range(10):
    print(*arr[i])