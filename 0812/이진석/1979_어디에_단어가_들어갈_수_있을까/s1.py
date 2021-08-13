import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = []
    cnt = 0
    for _ in range(N):  # 입력받은 배열
        arr.append(list(map(int, input().split())))

    for i in range(N):
        row_temp = 0    # 행 확인
        col_temp = 0    # 열 확인
        for j in range(N):  # 인덱스의 값이 1일 때 연속성을 확인하고 K개만큼만 연속하는지 확인
            if arr[i][j]:
                row_temp += 1
            else :
                if row_temp == K:
                    cnt += 1
                row_temp = 0
            if arr[j][i]:
                col_temp += 1
            else :
                if col_temp == K:
                    cnt += 1
                col_temp = 0
        if row_temp == K:
            cnt += 1
        if col_temp == K:
            cnt += 1
    print('#{} {}'.format(tc, cnt))
