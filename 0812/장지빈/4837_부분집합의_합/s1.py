import sys
sys.stdin = open('sample_input.txt')
#5팀 코드 참조
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split()) # N : 부분집합 수 K : 부분집합의 총합
    K_count = 0

    for i in range(1, 1 << 12):  # 공집합 제외, 2**12-1
        total = 0
        cnt = 0

        for j in range(12):
            if i & (1 << j):  # i의 원소에서의 부분집합들 ( i => 11 , j => 01, 10, 11)
                total += j + 1  # j가 0부터 시작이므로 +1
                cnt += 1

        if cnt == N and total == K: # 조건에 만족하는 부분집합들 카운트
            K_count += 1

    print('#{} {}'.format(tc, K_count))