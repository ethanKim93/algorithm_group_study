import sys
sys.stdin = open("sample_input.txt")

T = int(input())
arr = [_ for _ in range(1,13)]

for tc in range(1,T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        total = cnt = 0
        for j in range(12):
            if i & (1<<j):
                cnt += 1
                total += arr[j]
        if cnt == N and total == K:
            result += 1
    print('#{} {}'.format(tc, result))