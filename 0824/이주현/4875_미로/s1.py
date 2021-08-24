import sys
sys.stdin = open('sample_input.txt', 'r')

def navi(row, col):
    check.append((row, col))
    result = 0
    for idx in range(4):
        # 인덱스 범위 내에 있거나, 방문한 적이 없는경우
        if 0 <= row + delta_y[idx] < len(matrix) \
                and 0 <= col + delta_x[idx] < len(matrix) \
                and check[len(check) - 2] != (row + delta_y[idx], col + delta_x[idx]):
            # 길일 경우
            if matrix[row + delta_y[idx]][col + delta_x[idx]] == '0':
                result += navi(row + delta_y[idx], col + delta_x[idx])
                check.pop()
            # 목적지 일경우
            elif int(matrix[row + delta_y[idx]][col + delta_x[idx]]) > 1:
                return 1
    return result

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    delta_x = [0, 0, -1, 1]
    delta_y = [-1, 1, 0, 0]
    check = []
    start = 0
    for i in range(N):
        for j in range(N):
            if int(matrix[i][j]) > 1:
                start = (i, j)
                break
        if start:
            break

    print("#{} {}".format(tc, navi(start[0], start[1])))