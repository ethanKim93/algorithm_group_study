import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    ai = list(input().split())
    dif = []

    for a in range(0, N-M+1):
        result = 0
        for x in range(a, a+M):
            result += int(ai[x])
        dif.append(result)

    difMax = int(dif[0])
    difMin = int(dif[0])

    for y in dif:
        if y > difMax:
            difMax = y
        if y < difMin:
            difMin = y

    result = difMax - difMin
    print('#{} {}'.format(i+1, result))
