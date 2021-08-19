# (a+b)^n

# i 행 j 열
p = [[0]*10 for _ in range(10)]  # 문제의 조건에서 최대 10줄
for i in range(10):
    for j in range(i+1):
        if j == 0 or i == j:
            p[i][j] = 1  # 왼쪽 변 오른쪽 변은 1로 채우기
        else:
            p[i][j] = p[i-1][j-1] + p[i-1][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):   # 대각선상의 원소까지
            print(p[i][j], end=' ')
        print()

