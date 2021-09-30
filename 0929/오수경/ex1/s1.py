import sys
sys.stdin = open('input.txt')


nums = input()
idx = 0
while idx < len(nums):
    num = 0
    for i in range(idx, idx+7):
        num += int(nums[i])*(1 << (6-i%7))
    idx += 7
    print(num)