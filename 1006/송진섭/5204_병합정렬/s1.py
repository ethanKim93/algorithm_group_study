import sys
sys.stdin = open('sample_input.txt')


def merge(left, right):
    global cnt
    len_l = len(left)
    len_r = len(right)
    result = [0] * (len_l+len_r)
    i = right_i = left_i = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_i < len_l or right_i < len_r:
        if left_i < len_l and right_i < len_r:
            if left[left_i] < right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1
        elif left_i < len_l:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] = right[right_i]
            i += 1
            right_i += 1
    return result


def merge_sort(a_list):
    n = len(a_list)
    if n == 1:
        return a_list
    mid = n // 2
    left = a_list[:mid]
    right = a_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a_list = list(map(int, input().split()))
    cnt = 0
    print('#{} {} {}'.format(tc, merge_sort(a_list)[N//2], cnt))
