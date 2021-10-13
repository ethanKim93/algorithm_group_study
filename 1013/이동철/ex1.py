'''
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
'''


def dfs(adj):
    stack = [1]
    while stack:
        check = stack.pop()
        if visited[check] == 1:
            continue
        visited[check] = 1
        print(check, end=" ")
        for new_check in adj[check]:
            if not visited[new_check]:
                stack.append(new_check)
    return


edge = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

adj = [[] for _ in range(len(edge))]
for i in range(0, len(edge), 2):
    adj[edge[i]].append(edge[i + 1])
    adj[edge[i + 1]].append(edge[i])
print(adj)

visited = [0] * (len(set(edge)) + 1)
dfs(adj)


############################################################


#동호님 풀이
# # 7
# # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# N = int(input())
# E = list(map(int, input().split()))
# s = [0] * (N+1)
# visited = [0] * (N+1)
#
# top = -1
# def push_s(s, v):
#     global top
#     top += 1
#     s[top] = v
#
# def pop_s(s):
#     global top
#     top -= 1
#     return s[top+1]
#
# def DFS(V):
#     global s, top
#     push_s(s, V)
#     while not top == -1:
#         v = pop_s(s)
#         if not visited[v]:
#             visited[v] = 1
#             print(v, end=' ')
#             for w in link[v]:
#                 if not visited[w]:
#                     push_s(s, w)
#
#
# link = [[] for _ in range(N+1)]
# for i in range(0, len(E), 2):
#     link[E[i]].append(E[i+1])
#     link[E[i+1]].append(E[i])
# DFS(1)

# # 인접 리스트
# # adjL = [[0] * (N+1) for _ in range(N+1)]
# # for i in range(0, len(E), 2):
# #     adjL[E[i]][E[i+1]] = 1
# #     adjL[E[i+1]][E[i]] = 1

# print(adjL)


##############################################################


# 기웅님 풀이
# '깊이 우선탐색하여 경로를 출력하시오.'
# edge = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# edge = list(map(int, edge.split()))
# # 전체 노드 번호
# V = list(range(1,8))
# # 노드의 수
# N = len(V)
# # 인접행렬 정의
# adjM = [[0]*(N+1) for _ in range(N+1)]
# for i in range(len(edge)//2):
#     n1, n2 = edge[2*i], edge[2*i+1]
#     # 무방향 그래프로 인접행렬 초기화
#     adjM[n1][n2] = 1
#     adjM[n2][n1] = 1
#
# # stack 활용 깊이 우선탐색
# # 시작 정점을 1로 시작
# stack = [1]
# # 각 노드의 방문 여부를 정의할 리스트
# visited = [0]*(N+1)
# print('STACK 1:', end =' ')
# while stack:
#     v = stack.pop()
#     if not visited[v]:
#         print(v, end =' ')
#         visited[v] = 1
#         for n in range(1, N+1):
#             if adjM[v][n] and not visited[n]:
#                 stack.append(n)
# print()
#
# # stack 활용 깊이 우선탐색
# # push 할 때 방문 찍고 가기
# visited = [0]*(N+1)
# stack = [1]
# visited[1] = 1
# print('STACK 2:', end =' ')
# while stack:
#     v = stack.pop()
#     print(v, end =' ')
#     for n in range(1, N+1):
#         if adjM[v][n] and not visited[n]:
#             stack.append(n)
#             visited[n] = 1
# print()
#
# # 재귀 활용 깊이 우선탐색
# visited = [0]*(N+1)
# print('RECURSIVE:', end =' ')
#
#
# def dfs(v):
#     print(v, end=' ')
#     visited[v] = 1
#     for n in range(1, N+1):
#         if adjM[v][n] and not visited[n]:
#             dfs(n)
#
#
# dfs(1)
# print()



