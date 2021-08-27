import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    node, line = map(int, input().split()) # node: 노드의 갯수, line: 연결 선의 갯수
    maps = []
    for i in range(line):
        maps.append(list(map(int, input().split())))
    start, goal = map(int, input().split())

    temps = [[0] * (node + 1) for _ in range(node + 1)]

    # 인접행렬
    for i in range(line):
        temps[maps[i][0]][maps[i][1]] = 1
        temps[maps[i][1]][maps[i][0]] = 1

    visited = [0] * (node + 1)

    q = [start]

    # BFS
    while q:
        pos = q.pop(0)
        for i in range(1, node + 1): # 노드는 1부터 node의 갯수까지
            if temps[pos][i] == 1 and not visited[i]: # 인접행렬의 해당 행을 탐색 & 방문하지 않았으면
                q.append(i)
                visited[i] = visited[pos] + 1 # visited에 최단거리 기록

    print("#{} {}".format(tc, visited[goal])) # start~goal까지의 최단거리 출력
