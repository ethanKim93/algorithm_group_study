import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N = int(input())
    test_numbers = list(map(int, input().split()))
    min_num = test_numbers[0]
    max_num = test_numbers[0]
    for test_number in test_numbers:
        if min_num >= test_number:
            min_num = test_number
        if max_num <= test_number:
            max_num = test_number
    print('#{} {}'.format(i+1, max_num-min_num))