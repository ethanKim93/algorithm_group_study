import sys
sys.stdin = open('input.txt')
from pprint import pprint

# 지연님 코드
def find_set(n):
    while p[n] != n :
        n = p[n]
    return n

T = int(input())
for tc in range(1,T+1):
    # V 정점 수, E 간선 수
    V, E = map(int,input().split())
    # 가중치와 정점 담을 배열 arr 초기화
    arr = []
    for i in range(E):
        n1,n2,w = map(int,input().split())
        arr.append([w,n1,n2])               # 추후 정렬을 위해 순서를 바꿔서 append
    arr.sort()
    # 대표원소 초기화
    p = [i for i in range(V+1)]
    # 정점의 수를 카운트할 cnt와 가중치의 합을 구할 res 초기화
    cnt = res = 0
    for w,n1,n2 in arr :
        # n1과 n2의 대표원소가 다르다면, 즉, 사이클이 아니라면
        if find_set(n1) != find_set(n2):
            # 이 정점을 선택 -> cnt + 1
           cnt += 1
            # 가중치 +  -> 가중치가 낮은 순서대로 정렬한 배열이므로 자연스레 최소값
           res += w
            # n1과 n2 합치기
           p[find_set(n1)] = find_set(n2)
        # 선택한 정점의 수가 V와 같아진다면 break
        if cnt == V:
            break
    print('#{} {}'.format(tc,res))

# def bfs(v, w, cnt):
#     global ans
#     if w > ans:
#         return
#     if cnt == V:
#         if ans > w:
#             ans = w
#         return
#     for i in range(V+1):
#         if not visited[i] and adj[v][i]:
#             visited[i] = 1
#             bfs(i, w + adj[v][i], cnt+1)
#             visited[i] = 0
#     return
#
# for tc in range(1, int(input())+1):
#     ans = 987654321
#     V, E = map(int, input().split())
#     edge = [list(map(int, input().split())) for _ in range(E)]
#     # print(edge)
#     adj = [[0]*(V+1) for _ in range(V+1)]
#     visited = [0]*(V+1)
#     for i in range(E):
#         a, b, c = edge[i][0], edge[i][1], edge[i][2]
#         adj[a][b] = c
#         adj[b][a] = c
#     for i in range(V+1):
#         visited[i] = 1
#         bfs(i, 0, 0)
#         visited[i] = 0
#
#     print('#{} {}'.format(tc, ans))