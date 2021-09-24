import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def FS(head):
    if (head*2)>N:
        tree[head] = stack.pop(0)
    else:
        FS(head*2)
        if ((head*2)+1) <= N:
            FS((head*2)+1)

for tc in range(1,T+1):
    N = int(input())
    head = 1
    stack = [i for i in range(1,N+1)]
    tree = [0] * (N+1)
    FS(head)
    print(tree)
    #print('#{} {}'.format(tc, cnt))