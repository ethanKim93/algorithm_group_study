import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = sys.stdin.readline()
    nums = list(map(int, sys.stdin.readline().split()))



    big = 0
    for num in nums:
        if num > big:
            big = num

    small = nums[0]
    for num in nums[1:]:
        if num < small:
            small = num

    interval = big - small

    print('#{} {}'.format(tc, interval))
