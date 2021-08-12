import sys
sys.stdin = open('sample_input.txt')

T = int(input())
A = []
for num in range(1, 13):
    A.append(num)

for tc in range(1, T+1):
    N, K = map(int, input().split())
    subset_list = []
    cnt = 0
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
        subset_list.append(subset)

    for subset in subset_list:
        if len(subset) == N and sum(subset) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
