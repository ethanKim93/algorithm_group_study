import sys
sys.stdin = open('sample_input.txt')
# 부모노드는 왼쪽 자식 노드보다 커야하고 오른쪽 자식 노드보다 작아야함
# 왼쪽 서브트리 돌면서 넣어주기

def mktree(node):
    global cnt
    # 배열 안넘어가게 범위 설정해주기
    if node <= N:
        # 왼쪽
        mktree(node*2)
        # 더 못가면 넣어주기
        tree[node] = cnt
        cnt += 1

        # 오른쪽
        mktree((node*2) + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 1부터 시작하니가 N+1
    tree = [0] * (N+1)
    cnt = 1
    mktree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))