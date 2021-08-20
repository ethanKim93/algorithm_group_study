import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    T, E = map(int,input().split())
    input_data = list(map(int,input().split()))
    data = []
    for i in range(E):
        data.append(input_data[2*i:2*i+2])
    arr = [[] for _ in range(100)]
    for j in data:
        arr[j[0]].append(j[1])
    visited = [0]*100
    stack = [0]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = 1
            for v in arr[vertex]:
                if not visited[v]:
                    stack.append(v)
    if visited[99]==1:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))


    # stack = [S]
    # while stack:
    #     vertex = stack.pop()
    #     if not visited[vertex]:
    #         visited[vertex] = 1
    #         for v in matrix[vertex]:
    #             if not visited[v]:
    #                 stack.append(v)
