import sys
sys.stdin = open('input.txt')


def find_set(x):
    while x != p[x]:                    # 대표원소가 아니면
        x = p[x]                        # x가 가리키는 정점으로 이동
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))
edge.sort()                             # 가중치 기준 오름차순 정렬
p = [i for i in range(V+1)]             # 대표원소 초기화

N = V+1                                 # 0~V번 가지의 정점
cnt = 0
total = 0                               # 가중치의 합
for w, u, v in edge:
    if find_set(u) != find_set(v):      # 사이클을 만들지 않으면 선택
        cnt += 1
        total += w
        union(u, v)                     # v의 대표원소를 u의 대표원소로 바꿈
        if cnt == N-1:                  # N-1개의 간선을 선택하면 루프 종료
            break
print(total)