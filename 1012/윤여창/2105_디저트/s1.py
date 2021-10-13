#런타임에러 발생

import sys
sys.stdin = open('input.txt','r')

def route():
    for k in range(N - 1, 1, -1):
        for i in range(1, k):
            j = k - i
            for r in range(i, N - j):
                for c in range(N - i - j):
                    visited = [0] * 101
                    y, x = r, c
                    for d in range(4): 
                        n = j if d % 2 else i
                        for _ in range(n):  
                            y, x = y + dy[d], x + dx[d]
                            if not visited[matirx[y][x]]:
                                visited[matirx[y][x]] = True
                            else:  
                                break
                        else:
                            continue
                        break
                    else:  
                        return k * 2
    return -1


dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    matirx = [list(matirx(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, route()))