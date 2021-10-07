import sys
sys.stdin = open("sample_input.txt")

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return merge([arr[0]], [arr[1]])

    left = arr[0:len(arr)//2]
    right = arr[len(arr)//2:len(arr)]

    l = merge_sort(left)
    r = merge_sort(right)

    return merge(l, r)


def merge(left, right):
    global cnt
    left_N = len(left)
    right_N = len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    top = 0
    if left[-1] > right[-1]:
        cnt += 1

    while left_i < left_N or right_i < right_N:
        if left_i < left_N and right_i < right_N:
            if left[left_i] <= right[right_i]:
                result[top] = left[left_i]
                top += 1
                left_i += 1
            else:
                result[top] = right[right_i]
                top += 1
                right_i += 1

        elif left_i < left_N:
            result[top] = left[left_i]
            top += 1
            left_i += 1
        elif right_i < right_N:
            result[top] = right[right_i]
            top += 1
            right_i += 1

    return result

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    nums = merge_sort(nums)
    print('#{} {} {}'.format(tc, nums[N//2], cnt))




