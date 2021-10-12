import sys
sys.stdin = open("input.txt")

def quick_sort(li, start, end):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and li[left] <= li[pivot]:
            left += 1
        while right > start and li[right] > li[pivot]:
            right -= 1

        if left > right:
            li[pivot], li[right] = li[right], li[pivot]
        else:
            li[left], li[right] = li[right], li[left]

    quick_sort(li, start, right-1)
    quick_sort(li, right+1, end)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    A = list(map(int,input().split()))
    quick_sort(A, 0, n-1)
    print("#{} {}".format(tc, A[n//2]))

# Pass