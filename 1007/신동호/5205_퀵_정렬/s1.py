import sys
sys.stdin = open('sample_input.txt')

# Quick Sort
# Lomuto partition 알고리즘
def quickSort(l, r):
    global A
    if l < r:
        s = partition(l, r)  
        quickSort(l, s-1)
        quickSort(s+1, r)
    

def partition(p, r):
    global A
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quickSort(0, len(A)-1)
    print('#{} {}'.format(tc, A[len(A)//2]))