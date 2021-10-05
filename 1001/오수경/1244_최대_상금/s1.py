import sys
sys.stdin = open('input.txt')


# 모든 swap 가능한 경우
def change_nums(start, cnt):
    global ans
    if cnt == change:
        ans.append(int(''.join(nums)))
        return
    else:
        # cnt번 swap한 모든 순열 구하기 (cnt < change)
        for i in range(start, len(nums)-1):
            for j in range(i+1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                change_nums(start+1, cnt+1)
                nums[i], nums[j] = nums[j], nums[i]

        # change 만큼 swap 하지 않았는데 sorted 된 경우 -> 제일 작은 값들 swap 반복
        if nums == sorted(nums, reverse=True):
            while cnt != change:
                nums[-1], nums[-2] = nums[-2], nums[-1]
                cnt += 1
            ans.append(int(''.join(nums)))
            return

T = int(input())
for tc in range(1, T+1):
    nums_a, change_a = input().split()
    nums, change = list(nums_a), int(change_a)
    ans = []
    change_nums(0, 0)
    print('#{} {}'.format(tc, max(ans)))