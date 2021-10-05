import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 작업 횟수
    work = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    work = sorted(work, key=lambda x: (x[1]))
    i = 0
    while True:
        for j in range(i+1,N):
            if work[i][1] <= work[j][0]:
                cnt += 1
                i = j
                break
        if j == N-1:
            cnt += 1
            break

    print('#{} {}'.format(tc, cnt))

