def pascal(num):
    if num > 1:
        table[0] = [1]      # 초기배열
        table[1] = [1, 1]
        for i in range(2, num):
            table[i][0] = 1 # 처음과 끝은 1
            for j in range(1, i):   # i-1 배열의 j-1, j의 합으로 [i][j]를 구성
                table[i][j] = table[i - 1][j - 1] + table[i - 1][j]
            table[i][-1] = 1
    else:   # N이 1일때 한줄만 출력
        table[0] = [1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    table = [[0] * (n + 1) for n in range(N)]
    pascal(N)
    print('#{}'.format(tc))
    for i in range(N):
        print(*table[i])