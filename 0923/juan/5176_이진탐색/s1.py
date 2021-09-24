import sys
sys.stdin = open('sample_input.txt')


T = int(input())


def inorder(n):                                 # 중위 순회
    if n:
        inorder(left[n])
        tree.append(n)                          # 현재 노드 번호를 tree 배열에 추가
        inorder(right[n])


for tc in range(1, T+1):
    N = int(input())
    left = [0] * (N+1)                          # 왼쪽 자식 노드 번호 저장할 배열 초기화
    right = [0] * (N+1)                         # 오른쪽 자식 노드 번호 저장할 배열 초기화
    tree = []                                   # 중위순회하면서 처리되는 노드 순서 저장할 배열 초기화

    for i in range(2, N+1):
        if left[i//2]:                          # left 배열의 i//2번 인덱스(부모 노드 번호)에 값이 있으면
            right[i//2] = i                     # right 배열의 i//2번 인덱스에 현재 노드번호 할당
        else:                                   # left 배열의 i//2번 인덱스(부모 노드 번호)에 값이 없으면
            left[i//2] = i                      # left 배열의 i//2번 인덱스에 현재 노드번호 할당

    inorder(1)                                  # 중위 순회하면서 처리하는 노드 순서대로 tree 배열에 노드번호 추가
    for idx, num in enumerate(tree, start=1):
        if num == 1:                            # tree 배열 순회중 값이 1인경우의 인덱스가 루트 노드에 저장된 값
            root = idx
        if num == N//2:                         # tree 배열 순회중 값이 N//2인 경우의 인덱스가 N//2번 노드에 저장된 값
            half = idx
    print('#{} {} {}'.format(tc, root, half))