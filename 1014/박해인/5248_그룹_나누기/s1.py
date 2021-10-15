import sys
sys.stdin = open('sample_input.txt')

# 상호배타집합 make-set, find-set, union

# def make_set(x):  # 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
#     p[x] = x  # 노드 x의 부모 저장
#     rank[x] = 0  # 루트 노드가 x인 트리의 랭크 값 저장
#
def find_set(x):  # x를 포함하는 집합을 찾는 연산
    # 특정 노드에서 루트까지의 경로를 찾아 가면서 노드의 부모 정보를 갱신
    if x != p[x]
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):  # x와 y를 포함하는 두 집합을 통합하는 연산
    p[find_set(y)] = find_set(x)

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))
    p = [i for i in range(N+1)]  # parent

    for i in range(M):
        union(pairs[2*i], pairs[2*i+1])

    repr = []

    for i in range(N+1):
        repr[i] = find_set(i)
