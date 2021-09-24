import sys
sys.stdin = open('sample_input.txt')


T = int(input())


def inorder(node):                              # 중위 순회(어떤 순회든 상관없음)
    global cnt
    if node:
        inorder(left[node])
        cnt += 1                                # 노드마다 cnt에 1 추가
        inorder(right[node])


for tc in range(1, T+1):
    E,N = map(int, input().split())
    nodes = list(map(int, input().split()))
    cnt = 0                                     # 서브트리 노드의 개수 초기화

    left = [0] * (E+2)                          # 노드의 수 E+1개, 0번 인덱스 사용하지 않기위해 E+2 크기의 배열 초기화
    right = [0] * (E+2)

    for i in range(E):
        if left[nodes[i*2]]:                    # i*2번 인덱스(부모노드)의 왼쪽 자식 노드 값이 있는 경우에는 오른쪽 자식 노드에 노드 번호 할당
            right[nodes[i*2]] = nodes[i*2+1]
        else:                                   # i*2번 인덱스(부모노드)의 왼쪽 자식 노드 값이 없는 경우에는 왼쪽 자식 노드에 노드 번호 할당
            left[nodes[i*2]] = nodes[i*2+1]
    inorder(N)                                  # N번 노드를 루트로 하는 서브트리에서 (중위)순회하면서 노드의 개수 파악
    print('#{} {}'.format(tc, cnt))