import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    total_list = []
    total = 0
    result = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    total = arr[ni][nj] - arr[i][j]
                    if total < 0:
                        total = -(total)
                    total_list.append(total)

    for i in range(len(total_list)):
        result += total_list[i]
    print('#{} {}'.format(tc, result))



