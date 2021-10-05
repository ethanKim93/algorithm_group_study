import sys
sys.stdin = open('input.txt')

def in_order(v):
    if v <= N:
        in_order(2*v)
        print(node[v], end='')
        in_order(2*v + 1)

for tc in range(1,11):
    N = int(input())
    node = [[0] for _ in range(N+1)]
    for i in range(N):
        li = input().split()
        node[int(li[0])] = li[1]
    print('#{} '.format(tc), end='')
    in_order(1)
    print()