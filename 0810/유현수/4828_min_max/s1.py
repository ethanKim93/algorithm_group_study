import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    max_n = nums[0]
    for num in nums:
        if num > max_n:
            max_n = num

    min_n = nums[0]
    for num in nums:
        if num < min_n:
            min_n = num

    print('#{} {}'.format(tc, max_n-min_n))