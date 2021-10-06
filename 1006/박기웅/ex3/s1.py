# 트리 순회
# 전위, 중위, 후위 순회를 담을 배열 nodes
nodes = [[], [], []]
def traversal(n):
    if vtx[n]:
        nodes[0].append(n)
        traversal(left[n])
        nodes[1].append(n)
        traversal(right[n])
        nodes[2].append(n)
# 정점의 수
V = 12
edge = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
edge = list(map(int, edge.split()))

# 노드 번호의 최대값+1 로 count 배열 초기화
# left, right 인덱스 = 부모 노드 번호, 값 = 자식 노드 번호
vtx, left, right = [0]*14, [0]*14, [0]*14

for i in range(V):
    vtx[edge[i*2]] = 1
    vtx[edge[i*2+1]] = 1
    if not left[edge[i*2]]:
        left[edge[i*2]] = edge[i*2+1]
    else:
        right[edge[i*2]] = edge[i*2+1]
traversal(1)
for i, order in enumerate(['전위','중위','후위']):
    print(order,':', nodes[i])
