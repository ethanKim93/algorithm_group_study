import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())))[::-1]
    truck = sorted(list(map(int, input().split())))[::-1]
    maxV = 0

    t = windex = 0
    while windex < N and t < M:
        if truck[t] >= W[windex]:
            maxV += W[windex]
            t += 1
        windex += 1
    print('#{} {}'.format(tc, maxV))