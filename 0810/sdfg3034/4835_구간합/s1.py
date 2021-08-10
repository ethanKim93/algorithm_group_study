import sys
sys.stdin = open('input.txt')

T=int(input())
for i in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    for j in range(N-M+1):
        sum_number = 0
        for k in range(M):
            sum_number += numbers[j+k]
        if j == 0:
            max_nums = sum_number
            min_nums = sum_number
        if j != 0:
            if sum_number > max_nums:
                max_nums = sum_number
            if sum_number < min_nums:
                min_nums = sum_number
    print('#{0} {1}'.format(i,max_nums-min_nums))


