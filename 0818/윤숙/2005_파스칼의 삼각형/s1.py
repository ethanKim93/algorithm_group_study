
# 구조가 이런식도 가능하다..
# (a+b)=1
# (a+b)^1=1a+1b
# (a+b)^2=1a^2+2ab+1b^2
# (a+b)3=1a^3+3a^2b+3ab^2+1b^3

# j==0 ->1 i==j -> 1
# p[i-1][j] , p[i-1][j-1], i>j



p = [[0] * 10 for _ in range(10)]  # 문제조건에서 최대 10줄
for i in range(10):
    for j in range(i + 1):
        if j == 0 or i == j:
            p[i][j] = 1
        else:
            p[i][j] = p[i - 1][j - 1] + p[i - 1][j]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1): #대각선상의 원소까지
            print(p[i][j], end=' ')
        print()