import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    check = N*N*[0] + [0]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                a = matrix[i][j]
                vx = i + dx[k]
                vy = j + dy[k]

                if vx >= 0 and vx < N and vy >= 0 and vy < N:
                    if matrix[vx][vy] == a + 1:
                        check[a] += 1
    i = len(check)-1
    cnt = 1
    max_min = 0
    index = 0
    while i >= 0:
        if check[i] == 1:
           cnt += 1
        else:
            if max_min <= cnt:
                max_min = cnt
                index = i
            cnt = 1
        i -= 1
    print('#{} {} {}'.format(tc, index+1, max_min))


