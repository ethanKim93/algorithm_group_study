import sys
sys.stdin = open('sample_input.txt', 'r')


def partition(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt
    left_len = len(left)
    right_len = len(right)

    lst = [0] * (left_len + right_len)
    left_idx, right_idx = 0, 0
    idx = 0
    if left[-1] > right[-1]:
        cnt += 1

    while left_idx < left_len or right_idx < right_len:
        if left_idx < left_len and right_idx < right_len:
            if left[left_idx] <= right[right_idx]:
                lst[idx] = left[left_idx]
                idx += 1
                left_idx += 1
            else:
                lst[idx] = right[right_idx]
                idx += 1
                right_idx += 1
        elif left_idx < left_len:
            lst[idx] = left[left_idx]
            idx += 1
            left_idx += 1
        elif right_idx < right_len:
            lst[idx] = right[right_idx]
            idx += 1
            right_idx += 1

    return lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    result = partition(arr)

    print('#{} {} {}'.format(tc, result[N // 2], cnt))


# 슬라이싱 때문에 시간 초과의 문제
# def merge(left, right):
#     global cnt
#     result = []
#
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#
#     return result