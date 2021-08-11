import sys
sys.stdin = open("input.txt")

#상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1,int(input())+1):
    N = int(input())
    arr2d = [list(map(int, input().split())) for _ in range(N)]
    tot = 0
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if (0 <= ni < N) and (0 <= nj < N):
                    tot += abs(arr2d[i][j] - arr2d[ni][nj])

    print('#{} {}'.format(tc, tot))

