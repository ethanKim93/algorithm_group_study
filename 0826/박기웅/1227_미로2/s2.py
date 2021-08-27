import sys
sys.stdin = open("input.txt")

def bfs(S):
    q = [[] for _ in range(100**2)]     # 큐 생성 임의의 큰 개수로
    front = rear = -1                   # 초기화

    rear += 1                           # enqueue
    q[rear].append(S)

    while front!=rear:                  # 큐가 비었으면 끝남
        front += 1                      # dequeue
        i, j = q[front][0]
        visited[i][j] = 1

        if miro[i][j] == '3':
            return 1

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(100) and nj in range(100) and not visited[ni][nj]:
                if miro[ni][nj] == '0' or miro[ni][nj] =='3':
                    visited[ni][nj] = 1         # 방문 체크
                    rear += 1                   # enqueue
                    q[rear].append([ni, nj])
    return 0


for _ in range(1, 11):
    tc = input()
    miro = [list(input()) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상, 하, 좌, 우

    for i in range(100):
        for j in range(100):
            if miro[i][j] == '2':
                S = [i, j]

    print('#{} {}'.format(tc, bfs(S)))