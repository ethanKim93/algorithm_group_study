import sys
sys.stdin = open('sample_input.txt')


def tree(n):
    arr.append(n)
    idx = len(arr) - 1
    while idx > 1 and arr[idx] < arr[idx // 2]:
        arr[idx], arr[idx // 2] = arr[idx // 2], arr[idx]
        idx //= 2


T = int(input())
for tc in range(T):
    answer = 0
    N = int(input())
    NS = list(map(int, input().split()))
    arr = [0]
    for i in NS:
        tree(i)
    result = 0
    val = N // 2
    while val:
        result += arr[val]
        val //= 2
    print('#{} {}'.format(tc + 1, result))
