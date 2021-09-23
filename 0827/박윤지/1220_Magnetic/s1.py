# i, j 잘못 써서 헤맮....

import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # 1은 아래로, 2는 위로
    result = 0
    for j in range(N):
        col = []
        for i in range(N):
            elem = table[i][j]
            if len(col) > 0:
                if col[-1] == 1:
                    if elem == 2:
                        col.append(elem)
                if col[-1] == 2:
                    if elem == 1:
                        col.append(elem)
            else:
                if elem == 1:
                    col.append(elem)
        result += len(col) // 2
    print('#{} {}'.format(tc, result))