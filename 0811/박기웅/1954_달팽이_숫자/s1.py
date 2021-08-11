import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    # 우, 하, 좌, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # (0, -1)부터 출발
    i = cnt = k = 0
    j = -1
    arr2d = [[0]*N for _ in range(N)]
    while(cnt < N*N):
        ni, nj = i+di[k], j+dj[k]
        if (0 <= ni < N) and (0 <= nj < N) and (not arr2d[ni][nj]):
            cnt += 1
            arr2d[ni][nj] = cnt
            i, j = ni, nj
        else:
            k = (k+1)%4

    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, arr2d[i])))
