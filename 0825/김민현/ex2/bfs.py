"""
bfs - 인접 행렬 or 인접 리스트 구현
"""

def bfs(v):
    # while Q:
    #     #시작 위치 입력,visit에 입력
    #     #인접 노드 찾기
    #     for i in range(V+1):
    #         visit[v] = 1
    #         for j in range(V+1):
    #             # visit 방문한적이 없다면
    #             if adj[i][j] == 1 and visit[j] == 0:
    #                 # Q에 인접 노드 입력
    #                 Q.append(j)
    #                 visit[j] = 1
    #         # 시작 위치를 Q 가장 처음값으로 변경
    #         v = Q.pop(0)
    #         a = Q
    #         b = visit
    #         print(v)
    q = [v]

#인접 행렬
    # while q:
    #     v = q.pop(0)
    #     if not visited[v]:
    #         visited[v] = 1
    #         print(v, end=' ')
    #         for w in range(1,V+1):
    #             if adj[v][w] and not visit[w]
    #                 q.append(w)

#인접 리스트
   while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in adjlist[v]:
                if not visit[w]:
                    q.append(w)




import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V,E = map(int,input().split())
# 간선 정보 초기화
node = list(map(int,input().split()))

# Graph 초기화
#인접 행렬
#adj =[[0]*(V+1) for _ in range(V+1)]
# for i in range(E):
#     ni,nj = node[2*i], node[2*i+1]
#     adj[ni][nj] = 1
#     adj[nj][ni] = 1

adjlist = [[] for _ in range(V+1)]
for i in range(E):
    adjlist[node[i*2]].append(node[i*2+1])
#print(adjlist)


# 방문 표시 초기화
visit = [0]*(V+1)
# bfs 탐색 시작
bfs(1)