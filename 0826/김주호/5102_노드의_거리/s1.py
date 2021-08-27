import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    V, E = map(int, input().split())

    node = [[] for _ in range(V)]
    place = [0] * V
    queue = []

    for _ in range(E):
        n, m = map(int, input().split())
        node[n - 1].append(m - 1)
        node[m - 1].append(n - 1)

    S, G = map(int, input().split())
    S -= 1
    G -= 1

    queue.append(S)
    place[S] = 1
    front = -1
    rear = 0

    while front != rear:
        front += 1
        if place[G]:
            break
        while node[queue[front]]:
            if not place[node[queue[front]][0]]:
                queue.append(node[queue[front]][0])
                place[node[queue[front]][0]] = place[queue[front]] + 1
                rear += 1
            del(node[queue[front]][0])

    print("#{} {}".format(case + 1, place[G] - 1 if place[G] != 0 else 0))
