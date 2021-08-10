import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(N-M+1):
        s = 0
        for j in range(M):
            s += nums[i+j]      # s => 1+2+3 / 2+3+4 / 3+4+5...
        if not i:
            max_sum = s
            min_sum = s
        elif max_sum < s:
            max_sum = s
        elif min_sum > s:
            min_sum = s

    print('#{} {}'.format(tc, max_sum-min_sum))