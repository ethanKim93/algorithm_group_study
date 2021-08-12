import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N-1):
        min_i = i
        for j in range(i+1, N):
            if nums[min_i] > nums[j]:
                min_i = j
        nums[min_i], nums[i] = nums[i], nums[min_i]

    print('#{} {}'.format(tc, ' '.join(map(str, nums))))

