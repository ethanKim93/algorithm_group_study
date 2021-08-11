import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_num = 0
    for i in nums:
        if i > max_num:
            max_num = i

    min_num = max_num
    for j in nums:
        if j < min_num:
            min_num = j

    print('#{} {}'.format(tc, max_num - min_num))



