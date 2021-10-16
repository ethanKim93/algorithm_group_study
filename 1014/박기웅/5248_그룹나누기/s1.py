import sys
sys.stdin = open('sample_input.txt')

# def link(x, y):
#     if rank[x] > rank[y]:
#         rep[y] = x
#     else:
#         rep[x] = y
#         if rank[x] == rank[y]:
#             rank[y] += 1

# def union(x, y):
#     link( find_set(x), find_set(y))

def union(x, y):
    rep[find_set(x)] = find_set(y)

def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    # 상호 배타 집합 
    rep = list(range(N+1))

    # 페어를 하나로 만드는 합집합 연산
    for i in range(M):
        union(pair[2*i], pair[2*i+1])

    # 각 번호의 대표를 루트 노드로 갱신
    for i in range(1, N+1):
        rep[i] = find_set(i)

    print('#{} {}'.format(tc, len(set(rep[1:]))))