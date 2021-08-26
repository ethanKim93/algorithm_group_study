import sys
sys.stdin = open('sample_input.txt')


def bfs(queue):
    cnt = 1
    while queue:
        empty_lst = []
        while queue:
            node = queue.pop()
            for i in line[node]:
                if i == E:
                    return cnt
                if visited[i]:
                    continue
                empty_lst.append(i)
                visited[i] = 1
        cnt += 1
        queue = empty_lst
    return 0


T = int(input())
for tc in range(0, T):
    V, E = map(int, input().split())

    line = []
    for _ in range(V + 1):
        line.append([])
    visited = []
    for _ in range(V + 1):
        visited.append(0)

    for _ in range(E):
        a, b = map(int, input().split())
        line[a].append(b)
        line[b].append(a)

    S, E = map(int, input().split())
    visited[S] = 1
    print('#{} {}'.format(tc + 1, bfs([S])))