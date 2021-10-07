import sys
sys.stdin = open('input.txt')

T = int(input())

def merge(left_lst, right_lst):
    global cnt
    result = []
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst.pop(0))
            else:
                result.append(right_lst.pop(0))

        elif len(left_lst) > 0:
            result.append(left_lst.pop(0))
        elif len(right_lst) > 0:
            result.append(right_lst.pop(0))

    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left = []
    right = []
    middle = len(arr)//2
    for i in range(0, middle):
        left.append(arr[i])
    for i in range(middle, len(arr)):
        right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(arr)[N//2], cnt))
