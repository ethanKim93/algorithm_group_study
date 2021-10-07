import sys
sys.stdin = open('input.txt')
T = int(input())


def MergeSort(arr):
    global cnt
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left= MergeSort(arr[:mid])
    right=MergeSort(arr[mid:])

    if left[-1] > right[-1]:
        cnt+=1

    result=[]
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)
    return  result




for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    l = 0
    cnt=0
    r = len(arr)
    print(MergeSort(arr))
    print(cnt)