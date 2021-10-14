import sys
sys.stdin = open("sample_input.txt")


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    distance = [0] + [987654321 for _ in range(N)]
    node = [[] for _ in range(N + 1)]
    visited = [0] * (N+1)

    for _ in range(E):
        tmp1, tmp2, w = map(int, input().split())
        node[tmp1].append((tmp2, w))

    queue = [(0, 0)]

    while queue:
        idx, d = queue.pop(0)

        if visited[idx]:
            continue

        visited[idx] = 1
        for n_idx, nd in node[idx]:
            if distance[n_idx] > d + nd:
                distance[n_idx] = d + nd
                queue.append((n_idx, distance[n_idx]))

    print(distance[N])




