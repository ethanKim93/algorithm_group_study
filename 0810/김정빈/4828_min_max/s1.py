import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    i = 0
    mn, mx = ai[i], ai[i]
    for a in ai:
        if a < mn:
            mn = a
            i+=1
        if a > mx:
            mx = a
            i+=1

    print('#{} {}'.format(tc, mx-mn))