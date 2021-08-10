import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test in range(T):
    N = int(input())
    test_nums = list(map(int,input()))
    max_number = 0
    max_count = 0
    number_cnt = [0]*10

    for num in test_nums:
        number_cnt[num] += 1

    for i in range(10):
        if number_cnt[i] >= max_count:
            max_count = number_cnt[i]
            max_number = i

    print('#{} {} {}'.format(test+1, max_number, max_count))