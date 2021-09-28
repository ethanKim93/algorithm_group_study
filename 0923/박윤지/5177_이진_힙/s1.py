import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    NList = [0] + list(map(int, input().split()))
    # 이진최소힙 만들기
    tree = [0] * (N+1)
    tree[1] = NList[1]
    for i in range(2, N+1):
        tree[i] = NList[i]
        while i != 1:
            if tree[i] < tree[i//2]:
                temp = tree[i]
                tree[i] = tree[i//2]
                tree[i//2] = temp
                i //= 2
            else:
                break
    # 조상 노드의 합 구하기
    total = 0
    while N != 0:
        N //= 2
        total += tree[N]
    print('#{} {}'.format(tc, total))
