## 시간 초과

import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    global cnt
    result = []
    
    if left[-1] > right[-1]:
        cnt += 1

    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0] > right[0]:
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    left = []
    right = []
    mid = len(arr)//2
    for i in range(mid):
        left.append(arr[i])
    for j in range(mid,len(arr)):
        right.append(arr[j])
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int,input().split()))
    cnt = 0
    sort_list = merge_sort(li)
    value = sort_list[N//2]

    print('#{} {} {}'.format(tc, value, cnt))
