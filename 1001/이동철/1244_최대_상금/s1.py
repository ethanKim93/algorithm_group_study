import sys
sys.stdin = open('input.txt', 'r')


def change(c, idx):
    if c == 0:
        global result
        number = int(''.join(nums))
        if result < number:
            result = number
        return
    if nums[idx] < max(nums[idx + 1:]):
        for j in range(idx + 1, len(nums)):
            if nums[j] == max(nums[idx + 1:]):
                nums[idx], nums[j] = nums[j], nums[idx]
                change(c - 1, idx + 1)
                nums[idx], nums[j] = nums[j], nums[idx]
    else:
        if idx == len(nums) - 2:
            if len(set(nums)) < len(nums):
                change(0, idx)
            else:
                if c % 2:
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                    change(0, idx)
                    nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
                else:
                    change(0, idx)
        else:
            change(c, idx + 1)


for test_case in range(1, int(input()) + 1):
    num, cnt = input().split()
    cnt = int(cnt)
    nums = list(num)
    result = 0

    change(cnt, 0)
    print('#{} {}'.format(test_case, result))