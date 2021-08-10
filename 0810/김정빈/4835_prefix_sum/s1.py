import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    ai = list(map(int,input().split()))

    for i in range(N-M+1):
        prefix = ai[i:M+i]
        totfix = 0 #각 prefix의 합

        maxfix = prefix[0]
        minfix = prefix[0]

        for tot in prefix:
            totfix += tot

    if totfix > maxfix:
        maxfix = totfix
    if totfix < minfix:
        minfix = totfix

    print('#{} {}'.format(tc, maxfix-minfix))