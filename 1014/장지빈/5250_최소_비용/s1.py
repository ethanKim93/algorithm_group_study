import sys
sys.stdin = open('input.txt')
from pprint import pprint
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def calc(x, y, gas):
    if x == epoint[0] and y == epoint[1]:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if gas < newmat[nx][ny]:
                if newmat[x][y] < newmat[nx][ny]:
                    newmat
                    calc(nx, ny, gas + 1 + newmat[nx][ny]-newmat[x][y])
                else:
                    calc(nx, ny, gas + 1)

def run(s, e):
    pass

for tc in range(1, int(input())+1):
    ans = 0
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    newmat = copy.deepcopy(mat)
    # pprint(mat)
    spoint = [0,0]
    epoint = [N,N]
    visited = [[0]*N for _ in range(N)]
    run(spoint, epoint)
    # pprint(newmat)



    print('#{} {}'.format(tc, ans))
