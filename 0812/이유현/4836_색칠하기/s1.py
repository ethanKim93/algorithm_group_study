import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    r = []
    b = []
    for i in range(N):
        if arr[i][4] == 1:
            for rx in range(arr[i][0], arr[i][2] + 1):
                for ry in range(arr[i][1], arr[i][3]+1):
                    r.append((rx, ry))

        elif arr[i][4] == 2:
            for bx in range(arr[i][0], arr[i][2] + 1):
                for by in range(arr[i][1], arr[i][3] + 1):
                    b.append((bx, by))

    cnt = 0
    for point in r:
        if point in b:
            cnt += 1

    print('#{} {}'.format(tc, cnt))