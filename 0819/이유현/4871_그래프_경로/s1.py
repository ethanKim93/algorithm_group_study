import sys
sys.stdin = open('sample_input.txt')


def dfs(start, end):
    # 경로를 담을 route 객체
    route = []
    # 시작점을 경로에 추가
    route.append(start)

    # 경로에 값이 존재하지 않을때 까지 반복
    while route:
        # 지금 현재 위치를 꺼내 now 객체에 할당
        now = route.pop()
        # 현재위치를 방문함을 표시
        visit[now] = 1

        for i in range(1, V+1):
            # 간선이 존재하고 방문하지 않았다면 이동가능경로이므로 경로에 추가
            if d[now][i] == 1 and visit[i] == 0:
                    route.append(i)
    # 만약 도착노드에 방문했다면 1 반환
    if visit[end] == 1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    d = [[0]*(V+1) for i in range(V+1)]
    visit = [0 for i in range(V+1)]

    for i in range(E):
        x, y = map(int, input().split())
        # 방향성이 있기 때문에 시작점에서 갈 수 있는 좌표만 1로 표기한다
        d[x][y] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, dfs(S, G)))
