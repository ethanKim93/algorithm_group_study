import sys

sys.stdin = open('input.txt')

T = int(input())


# N 행,열 수 / i , j 현재 위치

class Move:

    def __init__(self, n, i, j):
        self.n = n
        self.a = self.n - 2
        self.b = self.n - 3
        self.c = self.n - 2
        self.d = self.n - 3
        self.li = [[0] * self.n for _ in range(self.n)]
        self.di = [0, 1, 0, -1]
        self.dj = [1, 0, -1, 0]
        self.i = i
        self.j = j
        self.v = 1

    def right(self):
        for _ in range(self.a):
            self.j += self.dj[0]
            self.li[self.i][self.j] = self.v
            self.v += 1
        return self.li

    def left(self):
        for _ in range(self.b):
            self.j += self.dj[2]
            self.li[self.i][self.j] = self.v
            self.v += 1
        return self.li

    def up(self):
        for _ in range(self.c):
            self.i += self.di[3]
            self.li[self.i][self.j] = self.v
            self.v += 1
        return self.li

    def under(self):
        for _ in range(self.d):
            self.i += self.di[1]
            self.li[self.i][self.j] = self.v
            self.v += 1
        return self.li


for tc in range(1, T + 1):
    N = int(input())
    result = [[0] * N for _ in range(N)]
    move_0 = Move(N+1, 0, -1)
    result += move_0.right()

    move_1 = Move(N+1, -1, N-1)
    result += move_1.under()

    move_2 = Move(N+2, N-1, N)
    result += move_2.left()

    ni, nj = move_2.i, move_2.j

    for m in range(3, N//3 + 3):
        move_m = Move(N, ni, nj)
        result += move_m.up()
        result += move_m.right()
        result += move_m.under()
        result += move_m.left()
        ni, nj = move_m.i, move_m.j
    move_l = Move(N, ni, nj)
    result += move_l.up()
    result += move_1.right()

    print('#{}'.format(tc))
    for l in result:
        print(*l)

