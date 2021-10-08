import sys
sys.stdin = open('input.txt')
T = int(input())


def MergeSort(l, r):
    global cnt
    if r - l <= 1:
        return

    mid = (l + r) // 2
    print(mid) #2134 521347689
    MergeSort(l, mid)
    MergeSort(mid, r)





for tc in range(1, T + 1):
    N = int(input())
    tmp = [0] * N
    arr = list(map(int, input().split()))
    cnt = 0
    l = 0
    r = len(arr)
    MergeSort(l, r)
    print()