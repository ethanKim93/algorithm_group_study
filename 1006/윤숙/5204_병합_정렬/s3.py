import sys
sys.stdin = open('input.txt')

def mergeSort(s, e):

    if s + 1 == e:
        return

    mid = (s + e) // 2
    mergeSort(s, mid)
    mergeSort(mid, e)

    if arr[mid - 1] > arr[e - 1]:
        global cnt;
        cnt += 1



    i, j, k = s, mid, s
    while i < mid and j < e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]; j, k = j + 1, k + 1
    while i < mid:
        tmp[k] = arr[i]; i, k = i + 1, k + 1
    while j < e:
        tmp[k] = arr[j]; j, k = j + 1, k + 1
    for i in range(s, e):
        arr[i] = tmp[i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    mergeSort(0, N)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))