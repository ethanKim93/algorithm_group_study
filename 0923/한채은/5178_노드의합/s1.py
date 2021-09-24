import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    '''
    N:노드개수
    M:리프노드 개수
    L:값을 출력할 노드번호
    '''
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)  # 트리 만들기

    for i in range(M):  # 리프노드를 트리에 넣기
        n, v = map(int, input().split())    # 리프노드 번호, 값
        tree[n] = v

    # 0번째 인덱스 안쓰니까 0까지 돌면서
    for i in range(N, 0, -1):
        # 현재 노드의 값을 부모 노드에 더하기
        tree[i//2] += tree[i]

    print("#{} {}".format(tc, tree[L]))

