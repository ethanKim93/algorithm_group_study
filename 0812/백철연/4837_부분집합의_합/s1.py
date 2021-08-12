import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [number for number in range(1, 13)]
    total = 0
    for i in range(1 << len(arr)):
        sum = 0
        cnt = 0
        for j in range(len(arr)):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1
        if sum == K and N == cnt:
            total += 1
    print('#{} {}'.format(tc, total))
