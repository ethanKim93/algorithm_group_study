def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    
    result = [0] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0
    while left_idx < len(left) or right_idx < len(right):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result[left_idx + right_idx] = left[left_idx]
                left_idx += 1
            else:
                result[left_idx + right_idx] = right[right_idx]
                right_idx += 1
        elif left_idx == len(left):
            for r in range(right_idx, len(right)):
                result[left_idx + r] = right[r]
            right_idx = len(right)
        elif right_idx == len(right):
            for l in range(left_idx, len(left)):
                result[l + right_idx] = left[l]
            left_idx = len(left)
    return result

def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)
    print("#{} {} {}".format(tc, arr[N//2], cnt))