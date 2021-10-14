import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    visited = [0] * (N+1)
    distance = [0] + [987654321 for _ in range(N)]
    nodes = [[] for _ in range(N+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        nodes[n1].append((n2, w))

    queue = [(0, 0)]

    while queue:
        idx, d = queue.pop(0)

        for node in nodes[idx]:
            n_idx, nd = node
            if distance[n_idx] > d + nd:
                distance[n_idx] = d + nd
                queue.append((n_idx, distance[n_idx]))

    print("#{} {}".format(tc, distance[N]))

