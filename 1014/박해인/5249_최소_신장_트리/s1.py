# 최소 신장 트리 : 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우
#  크루스칼
import sys
sys.stdin = open('sample_input.txt')

def find_set(x):  # x를 포함하는 집합을 찾는 연산
    # 특정 노드에서 루트까지의 경로를 찾아 가면서 노드의 부모 정보를 갱신
    while x != p[x]:  # 자기자신이 대표원소일 때 까지 반복
        x = p[x]
    return x

def union(x, y):  # x와 y를 포함하는 두 집합을 통합하는 연산
    p[find_set(y)] = find_set(x)

T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    data = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        data.append([w, n1, n2])
        # 가중치 오름차순으로 정렬을 위해 w를 앞에 배치
        # if not, use key=lambda x: x[2]
    data = sorted(data)
    # parent 부모 저장 변수
    p = [i for i in range(V+1)]  # p = list(range(V+1))
    res = 0
    for w, n1, n2 in data:
        if find_set(n1) != find_set(n2):
            res += w
            union(n1, n2)

    print('#{} {}'.format(test_case, res))