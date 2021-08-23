import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for i in range(9):
        row_sum = []
        col_sum = []
        for j in range(9):
            row_sum.append(arr[i][j])
            col_sum.append(arr[j][i])
        if sorted(row_sum) == [1, 2, 3, 4, 5, 6, 7, 8, 9] and sorted(col_sum) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            pass
        else:
            flag = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            area_sum = []
            for k in range(3):
                for l in range(3):
                    area_sum.append(arr[i + k][j + l])
            if sorted(area_sum) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                pass
            else:
                flag = 0
    print('#{} {}'.format(test_case,flag))