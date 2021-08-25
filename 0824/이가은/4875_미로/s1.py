import sys
sys.stdin = open('sample_input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def miro_find(miro, y, x):
    foot = miro[y][x]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if miro[b][a] == 3:


T = int(input())
for tc in range(T):
    N = int(input())

    miro = [list(input()) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                s_x = x
                s_y = y



    stack_x = []
    stack_y = []
    while True:
        if sx_

