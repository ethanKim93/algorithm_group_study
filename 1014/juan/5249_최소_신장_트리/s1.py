import sys
sys.stdin = open('sample_input.txt')


def find_set(x):                                    # 대표 노드를 찾는 함수
    return x if p[x] == x else find_set(p[x])


def union(x,y):                                     # 노드 간 병합하는 함수
    p[find_set(y)] = find_set(x)


def kruskal():                                      # 가중치 기준 정렬된 간선 중에 사이클을 제외한 낮은 가중치들을 순서대로 dist에 합산하는 kruskal 함수
    global dist
    for edge in mst:
        if find_set(edge[0]) != find_set(edge[1]):  # 연결하고자 하는 두 노드의 대표 노드가 다르면(사이클이 형성되지 않으면)
            dist += edge[2]                         # 그 간선을 dist에 합산
            union(edge[0], edge[1])                 # 두 노드를 병합


T = int(input())
for tc in range(1, T+1):
    V,E = map(int, input().split())
    mst = [list(map(int, input().split())) for _ in range(E)]
    mst.sort(key=lambda x: x[2])                    # 간선의 가중치 기준 오름차순 정렬
    p = [i for i in range(V+1)]                     # make_set
    dist = 0

    kruskal()
    print('#{} {}'.format(tc, dist))