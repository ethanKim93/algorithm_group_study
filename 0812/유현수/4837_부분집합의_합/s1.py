import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = range(1, 13)

    result = 0
    for i in range(1<<12):              # arr의 부분집합
        cnt = 0
        total = 0
        for j in range(13):
            if i & (1<<j):              # 개별 부분집합의 원소를 비트 연산자로 탐색
                cnt += 1                # 원소의 개수
                total += arr[j]         # 원소의 합
        if cnt == N and total == K:     # 원소가 N개, 합이 K일 경우 result += 1
            result += 1

    print('#{} {}'.format(tc, result))