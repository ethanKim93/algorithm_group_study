#인터넷
#https://kimmeh1.tistory.com/288
import sys
sys.stdin = open('sample_input.txt')


# D4 5249 최소 신장 트리

import sys
sys.stdin = open("input.txt")

test_case = int(input())
for tc in range(test_case):
    V, E = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())

        graph[a][b] = graph[b][a] = w

    INF = 987654321
    visited = [False] * (V+1)
    distance = [INF] * (V+1)

    cur_node = 0
    visited[cur_node] = True
    distance[cur_node] = 0

    connected_edge = 0
    while connected_edge < V:

        for next_node in range(V+1):
            if not visited[next_node] and graph[cur_node][next_node] \
                and graph[cur_node][next_node] < distance[next_node]:
                distance[next_node] = graph[cur_node][next_node]

        min_dist = INF
        for next_node in range(V+1):
            if not visited[next_node] and distance[next_node] < min_dist:
                min_dist = distance[next_node]
                cur_node = next_node

        visited[cur_node] = True
        connected_edge += 1

    answer = sum(distance)
    print("#{} {}".format(tc+1, answer))