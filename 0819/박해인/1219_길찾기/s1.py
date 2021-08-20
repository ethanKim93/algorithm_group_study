import sys
sys.stdin = open('input.txt')

def DFS():
    visited = [0] * 100
    stack = [0]
    visited[0] = 1  # 처음은 무조건 방문

    while stack:
        if stack[-1] == 99:  # 마지막 방문한 곳이 도착점이라면 1
            return 1

        # 방문하고, pop
        v = stack[-1]
        visited[v] = 1
        stack.pop()

        if adjacency.get(v, -1) != -1:
            for i in adjacency[v]:
                if visited[i] == 0:
                    stack.append(i)

    if visited[99]:
        return 1
    else:
        return 0


for _ in range(10):
    test_case, roads = map(int, input().split())
    pair_list = list(map(int, input().split()))

    adjacency = dict()  # 인접정보를 저장하는 dict
    for i in range(0, roads*2, 2):  # 99까지 받을 순 없으니 각 노드 별 경로를 저장하는 방식
        if adjacency.get(pair_list[i], -1) == -1:
            adjacency[pair_list[i]] = [pair_list[i+1]]
        else:  # key가 있으면 key 옆의 value append
            adjacency[pair_list[i]].append(pair_list[i+1])

    print('#{} {}'.format(test_case, DFS()))
