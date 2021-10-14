# 많이깨지는 규칙이 중간이어야하고
# 숫자가 중첩되어 있을 수록 많이 깰수 있다.
# 위에서 2칸씩 확인 하면서 어떤 수가 큰지 비교하고 그 수를 깬다.

# 깨지고 합쳐지는 건 되는 데 어디가 문제인지 모르겠습니당...
import sys

sys.stdin = open('input.txt')


def findtop():
    top = [[] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            if not top[j] and block[i][j]:
                top[j] = [j, i, block[i][j]]
    return top


def findMaxblock():
    for i in range(len(top)):
        if top[i]:
            for k in range(1, top[i][2] + 1):
                for j in range(len(delx)):
                    cy = top[i][0] + (dely[j] * k)
                    cx = top[i][1] + (delx[j] * k)
                    if 0 <= cy < W and 0 <= cx < H and block[cx][cy]:
                        if block[top[i][1]][top[i][0]] < block[cx][cy]:
                            return top[i][1], top[i][0]
    return top[i][1], top[i][0]


def breakblock(x, y, tmp):
    for n in range(tmp):
        for j in range(len(delx)):
            cy = y + (dely[j] * n)
            cx = x + (delx[j] * n)
            if 0 <= cy < W and 0 <= cx < H and block[cx][cy]:
                tmp = block[cx][cy]
                block[cx][cy] = 0
                breakblock(cx, cy, tmp)


def gravityblock():
    for i in range(H - 2, -1, -1):
        for j in range(W):
            if i + 1 < H:
                if block[i][j] != 0 and block[i + 1][j] == 0:

                    for k in range(i + 1, H):
                        if k == H - 1 and block[k][j] == 0:
                            block[k][j] = block[i][j]

                        elif block[k][j] != 0:
                            block[k - 1][j] = block[i][j]
                            break

                block[i][j] = 0


delx = [0, 0, 1, -1]
dely = [1, -1, 0, 0]
T = int(input())
for tc in range(1):
    N, W, H = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    for i in range(N):
        top = findtop()
        x, y = findMaxblock()
        tmp = block[x][y]
        breakblock(x, y, tmp)
        gravityblock()
        print(block)
