import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    test = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    min_sum = 999999
    max_sum = -1
    for idx in range(len(num_list) - test[1]+1):
        sum_li = 0
        for sum_ran in range(test[1]):
            sum_li += num_list[idx+sum_ran]

        if sum_li > max_sum:
            max_sum = sum_li
        if sum_li < min_sum:
            min_sum = sum_li
    print('#{} {}'.format(tc, max_sum - min_sum))
