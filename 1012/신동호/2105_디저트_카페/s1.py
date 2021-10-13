import sys
sys.stdin = open('sample_input.txt')

def dessert(i, j, mode, a, b):
    global max_num, stack

    if mode == 0 or mode == 1:
        for dist in range(1, N):
            ni = i + d[mode][0] * dist
            nj = j + d[mode][1] * dist
            if ni in range(N) and nj in range(N):
                if mode == 0:
                    dessert(ni, nj, mode+1, dist, b)
                elif mode == 1:
                    dessert(ni, nj, mode+1, a, dist)
            else:
                break
    elif mode == 2:
        ni2 = i + d[2][0] * a
        nj2 = j + d[2][1] * a
        ni3 = i + d[3][0] * b
        nj3 = j + d[3][1] * b
        if ni2 in range(N) and nj2 in range(N) and ni3 in range(N) and nj3 in range(N):
            stack.append((ori_i, ori_j, a, b))
        return

T = int(input())

d = ((1, 1), (1, -1), (-1, -1), (-1, 1))

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_num = -1
    stack = []

    for i in range(N-2):
        for j in range(1, N):
            ori_i = i
            ori_j = j
            dessert(ori_i, ori_j, 0, 0, 0)

    while stack:
        oi, oj, a, b = stack.pop()
        cafe = []
        flag = 0
        for mode in range(4):
            if flag:
                break
            if not mode%2:
                k = a
            else:
                k = b
            for dist in range(k):
                oi += d[mode][0]
                oj += d[mode][1]
                if mat[oi][oj] not in cafe:
                    cafe += [mat[oi][oj]]
                else:
                    flag = 1
                    break

        if not flag:
            if max_num < len(cafe):
                max_num = len(cafe)



    print('#{} {}'.format(tc, max_num))
