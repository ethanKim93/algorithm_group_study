import sys
sys.stdin = open('sample_input.txt')

def inorder_traverse(T):
    global ind 
    if T <= N:
        inorder_traverse(2*T)
        ind += 1
        tree[T] = ind
        inorder_traverse(2*T+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    ind = 0
    inorder_traverse(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))