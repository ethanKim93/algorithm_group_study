import sys
sys.stdin = open('sample_input.txt')

def preorder_traverse(T):
    global cnt
    if T:
        cnt += 1
        preorder_traverse(left[T])
        preorder_traverse(right[T])

T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    link = list(map(int, input().split()))
    for i in range(len(link)//2):
        if not left[link[2*i]]:
            left[link[2*i]] = link[2*i+1]
        else:
            right[link[2*i]] = link[2*i+1]
    cnt = 0
    preorder_traverse(N)
    print('#{} {}'.format(tc, cnt))
