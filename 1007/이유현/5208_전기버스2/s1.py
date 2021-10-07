import sys
sys.stdin = open('sample_input.txt')


def bus(now, charge):
    global minV
    if charge > minV:
        return

    if now >= N-1:
        minV = charge
        return

    maxMove = M[now]
    for stop in range(maxMove, 0, -1):
        bus(now+stop, charge+1)


for tc in range(1, int(input())+1):
    M = list(map(int, input().split()))
    N = M.pop(0)

    minV = 987654321
    bus(0, -1)
    print('#{} {}'.format(tc, minV))