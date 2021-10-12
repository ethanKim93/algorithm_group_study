import sys
sys.stdin = open('sample_input.txt')
# 해결못함
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    judge = sorted([int(input()) for _ in range(N)])
    time = [0] * M
    Time = []
    for jud in judge:
        for i in range(1, M+1):
            time[i-1] = jud * i
        Time += time
    Time.sort()
    print('#{} {}'.format(tc, Time[M-1]))
