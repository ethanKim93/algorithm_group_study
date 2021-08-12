import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    kills = []
    for i in range(0, N-M+1):               # MxM 영역 이동시키기
        for j in range(0, N-M+1):
            kill = 0
            for k in range(0+i, M+i):       # MxM 영역의 숫자 합 구하기
                for l in range(0+j, M+j):
                    kill += arr[k][l]
            kills += [kill]

    max_kill = kills[0]                     # 최댓값 구하기
    for k in kills:
        if max_kill < k:
            max_kill = k

    print('#{} {}'.format(tc, max_kill))