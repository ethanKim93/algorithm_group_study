def partition(arr, start, end):
    pivot = arr[start]
    L, R = start, end

    while L <= R:
        while L <= R and arr[L] <= pivot:
            L += 1
        while L <= R and pivot <= arr[R]:
            R -= 1
        if L < R:
            arr[L], arr[R] = arr[R], arr[L]
    arr[start], arr[R] = arr[R], arr[start]
    return R

def quick_sort(arr, start, end):
    if start < end:                         # 교차하지 않는다면
        pivot = partition(arr, start, end)  # pivot 설정하고
        quick_sort(arr, start, pivot-1)     # 왼쪽 정렬
        quick_sort(arr, pivot+1, end)       # 오른쪽 정렬
    return arr

import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc, quick_sort(numbers, 0, len(numbers)-1)[N//2]))