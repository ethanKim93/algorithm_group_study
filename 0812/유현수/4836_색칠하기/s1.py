import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1 = [0] * N
    c1 = [0] * N
    r2 = [0] * N
    c2 = [0] * N
    color = [0] * N
    matrix = [[0] * 10 for i in range(10)]      # 10x10 매트릭스 초기화

    for i in range(N):
        r1[i], c1[i], r2[i], c2[i], color[i] = map(int, input().split())

    for i in range(N):      # 매트릭스에 빨간색이면 1, 파란색이면 2를 더한다.
        for j in range(r1[i], r2[i]+1):
            for k in range(c1[i], c2[i]+1):
                matrix[j][k] += color[i]

    purple = 0      # 매트릭스를 순회하며 값이 3이면 purple 개수를 늘린다.
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                purple += 1

    print('#{} {}'.format(tc, purple))