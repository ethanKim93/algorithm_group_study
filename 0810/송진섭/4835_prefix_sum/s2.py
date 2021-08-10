import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for k in range(0, T):
    NM = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    smax = 0
    smin = 0
    for i in range(NM[0]-NM[1]+1):
        result = 0
        for j in range(0, NM[1]):
            result += ai[i+j]
        if smin == 0:
            smin = result
        if result > smax:
            smax = result
        if result < smin:
            smin = result

    print('#{} {}'.format(k + 1, smax-smin))
