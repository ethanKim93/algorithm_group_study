"""
< 구글링으로 찾은 해답 >
dfs 함수 내부에 이중 for문으로 조합을 훨씬 간단하게 구현했다.
"""

import sys
sys.stdin = open('input.txt')


def dfs(d, cnt):
    global ans
    if cnt == n:
        # 기저 케이스 도달하면 이전에 입력받은 ans와 비교하여 더 큰 수를 ans에 저장
        ans = max(int("".join(nums)), ans)
        return
    for i in range(d, l):
        for j in range(i + 1, l):
            if nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i, cnt + 1)
                nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T + 1):
    nums, n = input().split()
    nums = list(nums)
    numbers = nums[:]
    n = int(n)
    l = len(nums)

    ans = 0
    exception = 0

    # 길이가 2이거나 처음부터 최댓값으로 들어오는 경우
    if len(nums) == 2 or nums == sorted(nums, reverse=True):
        # 교환 횟수가 홀수이면 끝 두자리 교환
        if n % 2:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        exception = int("".join(numbers))

    dfs(0, 0)

    if ans == 0:
        ans = exception
    print('#{} {}'.format(tc, ans))
