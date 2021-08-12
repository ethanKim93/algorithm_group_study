import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    start = 0
    for k in range(100):
        if matrix[99][k] == 2:
            j = k
            break

    i = 99

    while True:
        if j > 0 and matrix[i][j-1]: # 왼쪽
            while j > 0 and matrix[i][j-1]:
                j -= 1
            else:
                i -= 1

        elif j < 99 and matrix[i][j+1]: # 오른쪽
            while j < 99 and matrix[i][j+1]:
                j += 1
            else:
                i -= 1
        else:  # 둘다 아니면
            i -= 1
        if i == 0:  # 도착
            break
    print('#{} {}'.format(tc, j))

