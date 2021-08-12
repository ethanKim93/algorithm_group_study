import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for p in range(N):
        arr[p] = [0] + arr[p] + [0]
    arr.insert(0, [0]*(N+2))
    arr.insert(N+2, [0]*(N+2))         # 외곽에 0 을 추가
    for i in range(1,N+1):
        for j in range(1,N-M+2):
            arsum_row = 0
            arsum_col = 0
            for k in range(-1,M+1,1):
                if arr[i][j+k] and arr[i][j-1]==0 and arr[i][j+M]==0:
                    arsum_row += 1
                if arr[j+k][i] and arr[j-1][i]==0 and arr[j+M][i]==0:
                    arsum_col += 1
            if arsum_row == M:
                answer += 1
            if arsum_col == M:
                answer += 1
    print('#{} {}'.format(test_case,answer))