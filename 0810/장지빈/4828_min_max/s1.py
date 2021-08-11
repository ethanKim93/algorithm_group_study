import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for a in range(T):
    N = int(input())
    ai = list(map(int, input().split()))

    maxN = ai[0]
    minN = ai[0]

    for i in ai:
        if maxN <= i:
            maxN = i
        if minN >= i:
            minN = i

    result = maxN - minN
    print('#{} {}'.format(a+1, result))