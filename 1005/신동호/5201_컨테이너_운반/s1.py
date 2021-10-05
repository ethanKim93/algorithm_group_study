import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    WE = list(map(int, input().split()))
    TR = list(map(int, input().split()))
    WE.sort()
    TR.sort()
    tot = 0
    while TR:
        t = TR.pop()
        while WE:
            w = WE.pop()
            if w <= t:
                tot += w
                break
    print('#{} {}'.format(tc, tot))