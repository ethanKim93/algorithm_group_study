import sys
sys.stdin = open('input.txt')
from pprint import pprint
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def drop():     # 구슬 투하
    q = []
    for _ in range(N):
        for i in range(W):
            for j in range(H):
                if not matrix[i][j]:
                    delete(i, j, matrix)
                    gravity(i, j, matrix)

def delete():
    pass

def gravity(x, y, li):  # 중력 작용
    # 한 칸의 블럭에 들어올 수 있는 최대 크기 = 9, 10으로 변경하고 아래로 떙기기
    q = []
    while q:
        if not li[q[0][0]][q[0][1]] or



for tc in range(1, int(input())+1):
    ans = 0
    cnt = 0
    N, W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    # print(N, W, H)
    # pprint(matrix)
    drop()


    for i in range(H):
        for j in range(W):
            if matrix[i][j]:
                ans += 1


    print('#{} {}'.format(tc, ans))