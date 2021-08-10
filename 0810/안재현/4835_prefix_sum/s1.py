import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for a in range(0, T):
    NM = list(map(int, input().split()))
    ai = list(map(int, input().split()))

    max = 0
    min = 0

    for i in range(NM[0]-NM[1]+1):
        result = 0
        for j in range(0, NM[1]):
            result += ai[i+j]

        if min == 0:
            min = result
        if result > max:
            max = result
        if result < min:
            min = result

    print('#{} {}'.format(a + 1, max-min))
