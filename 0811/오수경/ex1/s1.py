import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for arr_a in range(N):
        arr.append(list(map(int, input().split())))


    total = 0
    interval = 0

    # 상 하 좌 우
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                dx = i + di[k]
                dy = j + dj[k]

                if (0 <= dx < N) and (0 <= dy < N):
                    interval = abs(arr[i][j] - arr[dx][dy])
                    total += interval


    print(total)


