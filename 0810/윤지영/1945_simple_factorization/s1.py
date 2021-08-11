import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0]*5
    nums = [2,3,5,7,11]
    i = 0
    for num in nums:
        while not N % num:
            if not N % num:
                cnt[i] += 1
                N //= num
        i += 1
    print('#{} {} {} {} {} {}'.format(tc, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4]))