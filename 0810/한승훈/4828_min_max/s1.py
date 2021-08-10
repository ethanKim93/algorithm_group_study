import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    L = int(input())
    N = list(map(int, input().split()))

    max_num = N[0]
    min_num = N[0]
    for idx in range(L):
        if N[idx] > max_num:
            max_num = N[idx]
        if N[idx] < min_num:
            min_num = N[idx]
    print('#{} {}'.format(tc, max_num-min_num))