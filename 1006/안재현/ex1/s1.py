import sys
sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    P = arr[len(arr) // 2]
    low, mid, high = [], [], []
    for num in arr:
        if num < P:
            low.append(num)
        elif num > P:
            high.append(num)
        else:
            mid.append(num)
    return quick_sort(low) + mid + quick_sort(high)


for tc in range(3):
    T = list(map(int,input().split()))

    print(quick_sort(T))