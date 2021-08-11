import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4): # di, dj의 개수
                if 0 <= i + di[k] <= N-1 and 0 <= j + dj[k] <= N-1:
                    minus_num = arr[i][j] - arr[i + di[k]][j + dj[k]]
                    if minus_num >= 0:
                        total += minus_num
                    else:
                        total -= minus_num
    print(total)
