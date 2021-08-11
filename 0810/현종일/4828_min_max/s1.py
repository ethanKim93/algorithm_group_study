import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    maxnum = nums[0]
    minnum = nums[0]
    for num in nums:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
    print('#{} {}'.format(tc,maxnum-minnum))