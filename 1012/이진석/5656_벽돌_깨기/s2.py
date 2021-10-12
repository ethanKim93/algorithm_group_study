import sys
import copy
from collections import deque

sys.stdin = open('sample_input.txt')
sys.setrecursionlimit(10000)

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
def shoot(col, cnt, arr):
    '''
    :param col: 구슬을 쏠 행
    :param cnt: 구슬을 쏜 횟수
    :return:
    '''
    global min_brick
    if cnt == N:
        brick = 0
        for i in range(W):
            for j in range(H):
                if temp_arr[j][i]:
                    brick += 1
                if brick >= min_brick:
                    return
        if min_brick > brick:
            min_brick = brick
            return

    for row in range(H):
        if temp_arr[row][col]:
            breaking(row, col, temp_arr)
            renewal(temp_arr)
            break
    else:
        if col == W-1:
            min_brick = 0
            return

    for idx in range(W):
        cnt += 1
        shoot(idx, cnt, temp_arr)
        cnt -= 1

def DFS(col, cnt, arr):
    temp_arr = copy.deepcopy(arr)

    for idx in range(W):
        shoot(idx, cnt + 1, temp_arr)


def breaking(r, c, arr):             # 벽돌 제거
    size = arr[r][c]-1
    arr[r][c] = 0
    if size < 1: return arr
    for d in delta:
        nr, nc = r, c
        temp = size
        while temp != 0:
            nr = nr + d[0]
            nc = nc + d[1]
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc]:
                breaking(nr, nc, arr)
            temp -= 1
    return arr

def renewal(arr):                  # 벽돌 아래로 내리기 (사이의 0 제거)
    for i in range(W):
        for j in range(H-1,-1,-1):
            if not arr[j][i]:
                for k in range(j-1, -1, -1):
                    if arr[k][i]:
                        arr[k][i], arr[j][i] = arr[j][i], arr[k][i]
                        break
    return arr

for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(H)]
    min_brick = W*H   # 남은 벽돌
    visited = [0] * W
    for i in range(W):
        temp_table = copy.deepcopy(table)
        shoot(i, 0, temp_table)
    print(min_brick)


    # if tc == 5:
    #     print(*table, sep='\n')
    #     print()
    #     breaking(0,0)
    #     print(*table, sep='\n')
    #     print()
    # if tc == 1:
    # print(min_brick)
    # 1. 떨어트릴 열 정하기(DFS)
    # 2. 벽돌 제거
    # 3. 벽돌 갱신(빈자리 채우기.)
    # a = copy.deepcopy(table)
    # if tc ==1 :
    #     a = breaking(1,4,a)
    #     a = renewal(a)
    #     print(a)