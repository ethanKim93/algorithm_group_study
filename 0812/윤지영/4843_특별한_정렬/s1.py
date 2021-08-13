import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    nums_1 = nums[:]
    result = ''
    for i in range(5):
        idx_max = idx_min = i
        for j in range(i+1, N):
            if nums[idx_max] < nums[j]:
                idx_max = j
        nums[idx_max], nums[i] = nums[i], nums[idx_max]
        for k in range(i+1, N):
            if nums_1[idx_min] > nums_1[k]:
                idx_min = k
        nums_1[idx_min], nums_1[i] = nums_1[i], nums_1[idx_min]
        result += str(nums[i]) + ' ' + str(nums_1[i]) + ' '

    print('#{} {}'.format(tc,result))




