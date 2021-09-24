import sys
sys.stdin = open('sample_input.txt')

def inorder(i):
    if i < N+1:
        inorder(i*2)
        tree.append(i)
        inorder(i*2+1)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0]
    inorder(1)
    root = tree.index(1)
    half = tree.index(N//2)
    print('#{} {} {}'.format(tc, root, half))



