import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test in range(T):
    V, E = map(int, input().split())

    graph = [[0] * V for _ in range(V)]
    for e in range(E):
        i, j = map(int, input().split())
        graph[i-1][j-1] = 1

    S, G = map(int, input().split())

    visited = [S-1]     # 방문지점 노드-1
    stack = [S-1]
    result = 0

    while stack:
        for i in range(V):
            if graph[stack[-1]][i] == 1:
                graph[stack[-1]][i] = 0
                stack.append(i)
                visited.append(i)

                if i == G-1:
                    result = 1
                    break

                break
        else:
            stack.pop(-1)
        if result:
            break


    print('#{} {}'.format(test+1, result))
