import sys
sys.stdin = open('sample_input.txt')

def minheap(i):
    # 최소힙이므로 부모노드가 자식노드보다 크면 바꾸기
    if i<0:
        if nodes[i] < nodes[i//2]:
            nodes[i], nodes[i//2] = nodes[i//2], nodes[i]
            minheap(i//2)
        else:
            minheap(i-1)
def sum_parents(N, s):
    if N:
        sum_parents(N//2, s+nodes[N//2])
    else:
        return s



for tc in range(1, int(input())+1):
    N = int(input())
    # heap = [0]*(N+1)
    nodes = [0]+list(map(int, input().split()))
    minheap(N)
    print(sum_parents(N, 0))
    print(nodes)



