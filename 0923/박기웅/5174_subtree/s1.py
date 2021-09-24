import sys
sys.stdin = open('sample_input.txt')

def subtree(N):
    global cnt
    while nodes[N]:
        n = nodes[N].pop()
        cnt += 1
        subtree(n)

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    nodes = [[] for _ in range(E+2)]
    cnt = 1
    for i in range(E):
        nodes[pairs[2*i]].append(pairs[2*i+1])
    subtree(N)
    print('#{} {}'.format(tc, cnt))

