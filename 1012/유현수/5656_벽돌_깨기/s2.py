def gravity(arr):
    for i in range(8, -1, -1):
        for j in range(10):
            if arr[i][j] and not arr[i+1][j]:
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]


def applyGravity(temp_list):
    for c in range(10):
        start_row = 0
        for r in range(10):
            if temp_list[r][c] == 0:
                for row_idx in range(r - 1, start_row - 1, -1):
                    temp_list[row_idx + 1][c] = temp_list[row_idx][c]
                    temp_list[row_idx][c] = 0
                start_row += 1
    return


arr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 2, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 5],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
]

applyGravity(arr)

for i in range(10):
    print(arr[i])