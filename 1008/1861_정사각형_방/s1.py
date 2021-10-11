import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    pos = [0] * (N ** 2 + 1)
    dis = [1] * (N ** 2 + 1)
    d = {
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    }

    for i in range(N):
        for j in range(N):
            pos[A[i][j]] = (i,j)
    
    maximum = 1
    for i in range(N ** 2, 1, -1):
        if (pos[i][0] - pos[i-1][0], pos[i][1] - pos[i-1][1]) in d:
            dis[i-1] = dis[i] + 1
            if dis[i-1] >= maximum:
                maximum = dis[i-1]
                ans = i-1
        
    print('#{} {} {}'.format(tc, ans, maximum))