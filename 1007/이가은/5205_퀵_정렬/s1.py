# 재귀 시간 초과
# import sys
# sys.stdin = open('sample_input.txt')

def quick(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in range(1, len(arr)):
        if pivot > arr[i]:
            left += [arr[i]]
        else:
            right += [arr[i]]

    left = quick(left)
    right = quick(right)

    return left + [pivot] + right

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    print('#{} {}'.format(tc, quick(A)[N//2]))
