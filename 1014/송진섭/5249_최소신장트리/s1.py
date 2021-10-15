"""
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append((w, u, v))
    edge.sort()                             # 가중치 기준 오름차순 정렬
    p = [i for i in range(V+1)]             # make_set

    N = V+1                                 # 0~V번 까지의 정점
    cnt = 0
    total = 0                               # 가중치의 합
    for w, u, v in edge:                    # N-1개의 간선 선택 루프
        if find_set(u) != find_set(v):      # 사이클을 형성하지 않으면 선택
            cnt += 1
            total += w                      # 가중치의 합
            p[find_set(v)] = find_set(u)    # v의 대표원소를 u의 대표원소로 바꿈
            if cnt == N-1:
                break
    print('#{} {}'.format(tc, total))
