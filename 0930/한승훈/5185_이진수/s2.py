import sys
sys.stdin = open('sample_input.txt')

def bit_cal(n):
    global ans
    for num in n:
        num = int(num, 16)
        for j in range(4):
            if num&(8>>j):
                ans += '1'
            else:
                ans += '0'
    return ans


T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    ans = ''
    print('#{} {}'.format(tc, bit_cal(nums)))