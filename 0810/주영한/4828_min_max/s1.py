import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = int(input())
    temp_list = list(map(int, input().split()))
    min_value = temp_list[0]
    max_value = temp_list[0]
    for i in range(nums):
        temp_num = temp_list[i]
        if min_value > temp_num:
            min_value = temp_num
        if max_value < temp_num:
            max_value = temp_num
    result = max_value - min_value
    print("#{} {}".format(tc, result))