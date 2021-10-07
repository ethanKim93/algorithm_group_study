import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    global cnt
    if left and right and left[-1] > right[-1]:
        cnt += 1
    mg = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mg.append(left[i])
            i += 1
        else:
            mg.append(right[j])
            j += 1
    # left, right 중 다 돌아서 남은게 없는 경우 나머지를 다 붙임
    mg.extend(right[j:])
    mg.extend(left[i:])
    
    return mg

def merge_sort(arr):
    length = len(arr)
    if length==1:
        return arr
    mid = length//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)


    print('#{} {} {}'.format(tc, arr[N//2], cnt))