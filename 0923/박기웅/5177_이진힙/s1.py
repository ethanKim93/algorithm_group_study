import sys
sys.stdin = open('sample_input.txt')

def minheap(i):
    # 최소힙이므로 부모노드가 자식노드보다 크면 바꾸기
    if nodes[i] < nodes[i//2]:
        nodes[i], nodes[i//2] = nodes[i//2], nodes[i]
        minheap(i//2)


for tc in range(1, int(input())+1):
    N = int(input())
    nodes = [0]+list(map(int, input().split()))
    for i in range(2, N+1):
        minheap(i)
    total = 0
    while N:
        total += nodes[N//2]
        N //= 2

    print('#{} {}'.format(tc, total))



