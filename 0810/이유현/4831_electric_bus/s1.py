import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for i in range(1, t+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    cnt = 0
    bus = 0

    for j in range(M+1):
        if bus + K >= N:
            break
        elif bus + K < station[j]:
            if station[j-1] + K >= station[j]:
                cnt += 1
                bus = station[j-1]
            else:
                cnt = 0
                break
        else:
            continue

    print('#{} {}'.format(i, cnt))

