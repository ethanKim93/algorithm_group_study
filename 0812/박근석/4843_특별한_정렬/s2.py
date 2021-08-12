import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        minmax = i
        for j in range(i+1, N):
            if i%2:
                if nums[minmax] > nums[j]:
                    minmax = j

                else:
                    if nums[minmax] < nums[j]:
                        minmax = j
        nums[i], nums[minmax] = nums[minmax], nums[i]
    print('#{} {}'.format(tc, ' '.join(map(str, nums[:10]))))