import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for i in range(1, t+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_sum = 0
    min_sum = 0
    for k in range(N - M + 1):
        num_sum = 0
        for j in range(M):
            num_sum += num_list[k + j]
        if not k:
            max_sum = num_sum
            min_sum = num_sum
        elif max_sum < num_sum:
            max_sum = num_sum
        elif min_sum > num_sum:
            min_sum = num_sum
        else:
            pass

    print('#{} {}'.format(i, max_sum - min_sum))

