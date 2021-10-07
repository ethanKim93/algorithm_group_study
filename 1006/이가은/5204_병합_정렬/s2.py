import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    global cnt
    result = []
    
    if left[-1] > right[-1]:
        cnt += 1

    i, j = 0, 0 
    while len(left)>i or len(right)>j:
        if len(left)>i and len(right)>j:
            if left[i] > right[j]:
                result += [right[j]]
                j += 1
            else:
                result += [left[i]]
                i += 1
        elif len(right) > j:
            result += [right[j]]
            j += 1
        else:
            result += [left[i]]
            i += 1

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

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
