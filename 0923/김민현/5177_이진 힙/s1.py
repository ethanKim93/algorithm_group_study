#혼자못품

import sys
sys.stdin = open("sample_input.txt")

def insert_heap(data):
    heap.append(data)
    index = len(heap) - 1
    while index > 1 and heap[index] < heap[index // 2]:
        heap[index], heap[index // 2] = heap[index // 2], heap[index]
        index //= 2


def get_sum_heap():
    value = 0
    idx = N // 2
    while idx:
        value += heap[idx]
        idx //= 2
    return value


for t in range(int(input())):
    answer = 0
    N = int(input())
    user_input = list(map(int, input().split()))
    heap = [0]
    for data in user_input:
        insert_heap(data)
    answer = get_sum_heap()

    print('#{} {}'.format(t + 1, answer))