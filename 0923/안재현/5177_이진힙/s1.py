import sys
sys.stdin = open('sample_input.txt')


def tree(data):
    heap.append(data)
    index = len(heap) - 1
    while index > 1 and heap[index] < heap[index // 2]:
        heap[index], heap[index // 2] = heap[index // 2], heap[index]
        index //= 2


T = int(input())
for tc in range(T):
    answer = 0
    N = int(input())
    NS = list(map(int, input().split()))
    heap = [0]
    for i in NS:
        tree(i)
    print(heap)
    result = 0
    if N % 2 == 0:
        val = N % 2
        while val:
            result = heap[val]
    print(result)
