import sys
sys.stdin = open("sample_input.txt")

def bfs():
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        for i in N[t]:
            if i == g:
                return visited[t]
            elif not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    return 0

for tc in range(1, int(input())+1):
    V,E = map(int, input().split())
    N = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = list(map(int, input().split()))
        N[n1].append(n2)
        N[n2].append(n1)
    s, g = map(int, input().split())
    queue = [s]
    visited = [0] * (V + 1)
    print('#{} {}'.format(tc, bfs()))
