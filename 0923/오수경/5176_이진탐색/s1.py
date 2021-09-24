import sys
sys.stdin = open('sample_input.txt')

def inorder_traverse(T):
    global cnt
    if T < N+1:
        inorder_traverse(2*T)
        tree_node[T] = cnt
        cnt += 1
        inorder_traverse(2*T+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree_node = [0] * (N+1)
    cnt = 1
    inorder_traverse(1)
    print(f'#{tc} {tree_node[1]} {tree_node[N//2]}')
