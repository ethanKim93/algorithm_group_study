import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    cnt = 0                         # 길이가 K인 경우의 수
    for i in range(N):
        row = 0                     # 가로 단어가 들어갈 수 있는 길이
        for j in range(N):
            if matrix[i][j]:        # 가로 순회
                row += 1            # 1을 만나면 row 1 증가
            else:                   # 0을 만나면 길이를 검사하고 row 0으로 초기화
                if row == K:
                    cnt += 1
                row = 0
        if row == K:                # 순회가 끝났을 때 길이 검사
            cnt += 1

    for i in range(N):
        col = 0                     # 가로 단어가 들어갈 수 있는 길이
        for j in range(N):
            if matrix[j][i]:        # 세로 순회
                col += 1            # 1을 만나면 col 1 증가
            else:                   # 0을 만나면 길이를 검사하고 col 0으로 초기화
                if col == K:
                    cnt += 1
                col = 0
        if col == K:                # 순회가 끝났을 때 길이 검사
            cnt += 1

    print('#{} {}'.format(tc, cnt))