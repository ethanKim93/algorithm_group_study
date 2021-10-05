import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    nums,N = input().split()
    N = int(N)
    nums = list(map(int,nums))
    cnt = 0
    idx = 0
    same_flag = 0
    same_cnt = 0

    while cnt < N:
        max_idx = idx
        if idx == len(nums)-1:
            if (N-cnt)%2 | same_flag:
                break
            else:
                nums[-1],nums[-2] = nums[-2],nums[-1]
                break
        else:
            for j in range(idx+1,len(nums)):
                if nums[max_idx] <= nums[j]:
                    max_idx = j
                if nums[max_idx] == nums[j]:
                    same_flag = 1
            if max_idx != idx:
                nums[max_idx],nums[idx] = nums[idx],nums[max_idx]
                cnt += 1
            idx += 1
        a = 1
    ans = ''
    for k in nums:
        ans += str(k)
    print('#{} {}'.format(tc,ans))