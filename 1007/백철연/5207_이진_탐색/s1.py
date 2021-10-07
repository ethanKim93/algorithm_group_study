import sys
sys.stdin = open('sample_input.txt')


def search(nums, t):
    left, right = 0, len(nums) - 1
    before = None
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < t:
            left = mid + 1

        elif nums[mid] > t:
            right = mid - 1

        else:
            return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    nums2 = list(map(int, input().split()))
    ans = 0
    for i in nums2:
        ans += search(nums, i)

    print('#{} {}'.format(tc, ans))