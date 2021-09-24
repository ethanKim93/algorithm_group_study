import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0]

    for num in arr:
        heap.append(num)
        while True:
            n = heap.index(num)
            p = n // 2
            if heap[p] > heap[n] and p:
                heap[p], heap[n] = heap[n], heap[p]
            else:
                break

    ans = 0
    idx = len(heap) - 1
    while idx:
        idx //= 2
        ans += heap[idx]

    print('#{} {}'.format(tc, ans))
