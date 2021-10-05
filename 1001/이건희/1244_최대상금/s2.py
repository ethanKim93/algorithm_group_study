import sys
import copy
sys.stdin = open("input.txt")

def dfs(k,cnt):
    global ans
    if cnt == pos:
        ans = max(int("".join(n)), ans)
        return

    for i in range(k, n_length):
        for x in range(i+1, n_length):
            if n[i] <= n[x]:
                n[i], n[x] = n[x], n[i]
                dfs(k,cnt+1)
                n[i], n[x] = n[x], n[i]

for tc in range(1,int(input())+1):
    n, pos = input().strip().split()
    n, pos = list(n), int(pos)
    n2 = copy.deepcopy(n)
    n_length = len(n)
    ans = 0

    str_n = ''.join(map(str,n))
    int_n = int(str_n)
    mx_n = int(''.join(map(str,sorted(n,reverse=True))))
    flag = 0
    if n_length == 2 or int_n == mx_n:
        cnt = 0
        while cnt < pos:
            n[-1], n[-2] = n[-2], n[-1]
            cnt += 1
        flag = int("".join(map(str,n)))

    cnt = 0
    dfs(0,cnt)
    if ans == 0:
        ans = flag
    print('#{} {}'.format(tc,ans))

# Fail: #10 Runtime Error

# def dfs(d, cnt):
#     global ret
#     if cnt == n:
#         ret = max(int("".join(nums)), ret)
#         return
#     for i in range(d, l):
#         for j in range(i + 1 , l):
#             if nums[i] <= nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 dfs(i, cnt + 1)
#                 nums[i], nums[j] = nums[j], nums[i]
#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     nums, n = input().split()
#     nums = list(nums)
#     numbers = nums[:]
#     n = int(n)
#     l = len(nums)
#     ret = 0
#     flag = 0
#     if len(nums) == 2 or nums == sorted(nums, reverse=True):
#         cnt = 0
#         while cnt != n:
#             numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
#             cnt += 1
#         flag = int("".join(numbers))
#     cnt = 0
#     dfs(0, cnt)
#     if ret == 0:
#         ret = flag
#     print("#" + str(test_case) + " " + str(ret))

#https://goodlucknua.tistory.com/58