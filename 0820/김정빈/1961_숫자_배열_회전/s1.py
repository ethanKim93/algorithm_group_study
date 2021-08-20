#1961. 숫자 배열 회전
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rc = [list(map(str, input().split())) for _ in range(N)]
    ans = [[''] * 3 for _ in range(N)]

    #90도
    idx = 0
    for i in range(N):
        for j in range(N):
            ans[i][idx] += rc[N-1-j][i]
    idx += 1

    #180도
    for i in range(N):
        for j in range(N):
            ans[i][idx] += rc[N-1-i][N-1-j]
    idx += 1

    # 270도
    for i in range(N):
        for j in range(N):
            ans[i][idx] += rc[j][N-1-i]

    print('#{}'.format(tc))
    for u in ans:
        print(*u)