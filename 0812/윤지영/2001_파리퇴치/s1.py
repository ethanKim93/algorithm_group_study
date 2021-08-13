import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    li = []
    for _ in range(N):
        li += [list(map(int, input().split()))]
    max_result = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for m in range(M):
                    result += li[i+k][j+m]
            if max_result < result:
                max_result = result
    print('#{} {}'.format(tc, max_result))


