import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt = 1
    li = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while cnt <= N*N:
        for i in range(0, N):
            for j in range(-1, N):
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    i, j = ni, nj
                    while (0 <= ni < N) and (0 <= nj < N) and (li[ni][nj] == 0):
                        li[ni][nj] = cnt
                        cnt += 1
                        ni = i + di[k]   # k = 0일때 조건 벗어날때까지 반복해야함
                        nj = j + dj[k]
                        i, j = ni, nj
                    i -= di[k]
                    j -= dj[k]  # 범위 벗어남 or 이미 숫자가 있는 곳이므로 후진
    print('#{}'.format(tc))
    for l in li :
        print(*l)

