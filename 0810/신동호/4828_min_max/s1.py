import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    min_n = numbers[0]
    max_n = numbers[0]
    for ind in range(N):
        if min_n > numbers[ind]:
            min_n = numbers[ind]
        if max_n < numbers[ind]:
            max_n = numbers[ind]
    print('#{} {}'.format(tc, max_n - min_n))
