import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_a = nums[0]
    min_a = nums[0]
    for i in nums:
        if i > max_a:
            max_a = i
    for i in nums:
        if i < min_a:
            min_a = i
    result = max_a - min_a
    print('#{} {}'.format(tc, result))
