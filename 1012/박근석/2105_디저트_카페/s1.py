import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

def check(i,j,d, group_cafe):
    global min_cafe, si, sj
    print(group_cafe)
    if i == si and j == sj and d == 3:
        if min_cafe <= len(group_cafe):
            min_cafe = len(group_cafe)
            group_cafe = []
            return

    group_cafe.append(matrix[i][j])

    for q in range(2):



        vx = i + dx[d+q]
        vy = j + dy[d+q]
        if 0 <= vx < N and 0 <= vy < N:
            if matrix[vx][vy] not in group_cafe:
                check(vx, vy, d+q, group_cafe)

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for i in range(N)]
    group_cafe = []
    min_cafe = 0

    for i in range(N):
        for j in range(N):
            si = i
            sj = j
            check(i,j,0, group_cafe)

    print(min_cafe)