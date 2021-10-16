# ....ㅎㅎ...
import sys
sys.stdin = open('sample_input.txt')

def cost_min():
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    A = 1000000

    dist = [[A]* N for _ in range(N)]
    dist[0][0] = 0

    queue = []
    queue.append((0,0))

    while queue:
        q = queue.pop(0)
        for i in range(4):
            ny = q[0] + dy[i]
            nx = q[1] + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                diff = 0
                if jido[ny][nx] > jido[q[0]][q[1]]:
                    diff = jido[ny][nx] - jido[q[0]][q[1]]

                if jido[ny][nx] > jido[q[0]][q[1]] + diff + 1:
                    jido[ny][nx] = jido[q[0]][q[1]] + diff + 1
                    queue.append((ny,nx))


    return dist[N-1][N-1]

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    jido = [list(map(int, input().split())) for _ in range(N)]

    result = cost_min()
    print('#{} {}'.format(tc, result))