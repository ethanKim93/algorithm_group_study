import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def partition(a, l, r):
    p = a[l]
    i = l
    j = r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

def quickSort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quickSort(a, l, s-1)
        quickSort(a, s+1, r)

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr,0,len(arr)-1)
    print('#{} {}'.format(tc, arr[N//2]))