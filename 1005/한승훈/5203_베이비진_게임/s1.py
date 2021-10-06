import sys
sys.stdin = open('sample_input.txt')


def babygin(lst):
    nums = [0] * 10
    for n in lst:
        nums[n] += 1
    for idx in range(0,len(nums)-2):
        if nums[idx] and nums[idx+1] and nums[idx+2]:
            return True
    for num in nums:
        if num == 3:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    ans = 0
    for idx, card in enumerate(cards):
        if idx % 2:
            p2.append(card)
        else:
            p1.append(card)
        if len(p1) >= 3:
            if babygin(p1):
                ans = 1
                break
        if len(p2) >= 3:
            if babygin(p2):
                ans = 2
                break
    print('#{} {}'.format(tc, ans))



