import sys
sys.stdin = open('sample_input.txt')


def heap(n):
    global idx
    heaparr[idx] = n
    temp = idx
    while temp > 1 and heaparr[temp] < heaparr[temp//2]:
        heaparr[temp], heaparr[temp//2] = heaparr[temp//2], heaparr[temp]
        temp = temp // 2
    idx += 1

def sum_heap():
    total = 0
    idx = N // 2
    while idx:
        total += heaparr[idx]
        idx = idx // 2
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heaparr = [0] * (N+1)
    idx = 1

    for n in arr:
        heap(n)

    print('#{} {}'.format(tc, sum_heap()))

