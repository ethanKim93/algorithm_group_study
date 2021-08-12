import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    nums_len = int(input())
    nums = list(map(int, input().split()))
    for j in range(nums_len-1, 0, -1):
        for i in range(nums_len-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    print('#{} '.format(tc), end='')
    print(*nums)