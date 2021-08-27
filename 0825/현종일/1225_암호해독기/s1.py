import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))

    while True:
        if nums[7] == 0:
            break

        for i in range(1, 6):
            if nums[0] > i:
                nums[0] -= i
                nums.append(nums.pop(0))
            else:
                nums[0] = 0
                nums.append(nums.pop(0))
                break

    print('#{}'.format(tc), end= " ")
    print(*nums)