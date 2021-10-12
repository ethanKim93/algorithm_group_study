import sys
sys.stdin = open('sample_input.txt')

def quicksort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quicksort(lst, l, s-1)
        quicksort(lst, s+1, r)

def partition(lst, l, r):
    pivot = lst[l]
    i, j = l, r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i = list(map(int, input().split()))
    quicksort(i, 0, len(i)-1)
    print('#{} {}'.format(tc, i[N//2]))
