import sys
sys.stdin = open('input.txt')


def inorder(node):                                  # 중위순회 함수
    if node:
        inorder(left[node])                         # 왼쪽 자식 노드 확인
        print(tree[node], end='')                   # 현재 노드 출력
        inorder(right[node])                        # 오른쪽 자식 노드 확인

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)                                # 알파벳을 저장할 트리 초기화
    left = [0]*(N+1)                                # 왼쪽 자식 노드
    right = [0]*(N+1)                               # 오른쪽 자식 노드

    for i in range(N):
        node = input().split()                      # 노드에 들어갈 정보
        if len(node) > 2:                           # 자식이 있는 경우
            left[int(node[0])] = int(node[2])       # 왼쪽 자식 노드에 노드 번호 입력
            if len(node) > 3:                       # 오른쪽 자식도 있는 경우
                right[int(node[0])] = int(node[3])  # 오른쪽 자식 노드에도 노드 번호 입력
        tree[int(node[0])] = node[1]                # 트리에 알파벳 입력

    print('#{}'.format(tc), end=' ')
    inorder(1)                                      # 중위 순회
    print()