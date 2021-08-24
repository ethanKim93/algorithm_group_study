import sys
sys.stdin = open('sample_input.txt', 'r')

def min_arr(i, tmp):
    global min_num
    if min_num < tmp:
        return

    if i == len(matrix):
        if min_num > tmp:
            min_num = tmp
        return

    for j in range(len(matrix)):
        if visited[j] != 1:
            tmp += matrix[i][j]
            visited[j] = 1
            min_arr(i+1, tmp)
            visited[j] = 0
            tmp -= matrix[i][j]



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 10 * N
    min_arr(0, 0)

    print("#{} {}".format(tc, min_num))