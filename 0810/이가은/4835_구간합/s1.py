import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test in range(T):
    num_cnt, rng = map(int, input().split())
    numbers_list = list(map(int, input().split()))

    min_sum_value = 1000000
    max_sum_valus = 0
    for i in range(num_cnt-rng+1):
        sum_value = 0
        for j in range(rng):
            sum_value += numbers_list[i+j]
        if min_sum_value > sum_value:
            min_sum_value = sum_value
        if max_sum_valus < sum_value:
            max_sum_valus = sum_value
    print('#{} {}'.format(test+1,max_sum_valus-min_sum_value))