import sys
sys.stdin = open("input.txt")

def LVR(n):
    if n:
        LVR(LEFT[n])
        print(di[n], end = '')
        LVR(RIGHT[n])

T = 10

for tc in range(1, T+1):
    N = int(input())
    LEFT = [0] * (N+1)
    RIGHT = [0] * (N+1)
    di = {}
    for _ in range(N):
        inf = list(input().split())
        di[int(inf[0])] = inf[1]
        if len(inf) == 3:
            LEFT[int(inf[0])] = int(inf[2])
        elif len(inf) == 4:
            LEFT[int(inf[0])] = int(inf[2])
            RIGHT[int(inf[0])] = int(inf[3])
    print('#{} '.format(tc), end='')
    LVR(1)
    print()