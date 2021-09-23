import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                for k in range(i+1,N):
                    if matrix[k][j] == 1:
                        break
                    if matrix[k][j] == 2:
                        matrix[k][j] = 0
                        ans += 1
                        break
    print('#{} {}'.format(tc,ans))

    #print(matrix)