import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))

    for i in range(N-1):
        idx_min = i
        for j in range(i,N):
            if nums[idx_min] > nums[j]:
                nums[idx_min], nums[j] = nums[j], nums[idx_min]
        idx_min = j
    print('#{} {}'.format(tc, ' '.join(map(str,nums))))
