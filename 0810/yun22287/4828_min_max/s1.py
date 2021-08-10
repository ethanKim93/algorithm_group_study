import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums_max = nums[0]
    nums_min = nums[0]
    for num in nums:
        if nums_max < num:
            nums_max = num
        if nums_min > num:
            nums_min = num
    result = nums_max - nums_min
    print('#{0} {1}'.format(tc, result))