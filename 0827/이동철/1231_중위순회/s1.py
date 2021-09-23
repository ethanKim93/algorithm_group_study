import sys
sys.stdin = open('input.txt')


# 중위
def inorder_traverse(n):
    global result
    if n:
        # 유효한 정점이라면
        inorder_traverse(left[n])  # n의 왼쪽 자식으로 접근
        result += word[n]
        inorder_traverse(right[n]) # n의 오른쪽 자식으로 접근


for tc in range(1, 11):
    V = int(input())
    # 트리의 정점의 총 개수

    result =''
    parent = [0] * (V + 1)
    word = [0] * (V + 1)
    left = [0] * (V + 1)
    right = [0] * (V + 1)

    for _ in range(V):
        edge = list(map(str,input().split()))   # 간선의 정보
        word[int(edge[0])] = edge[1]    # 단어 저장하기
        if len(edge) == 3:
            left[int(edge[0])] = int(edge[2])
            parent[int(edge[2])] = int(edge[0])
        elif len(edge) == 4:
            left[int(edge[0])] = int(edge[2])
            parent[int(edge[2])] = int(edge[0])
            right[int(edge[0])] = int(edge[3])
            parent[int(edge[3])] = int(edge[0])

    inorder_traverse(1)
    print('#{} {}'.format(tc, result))