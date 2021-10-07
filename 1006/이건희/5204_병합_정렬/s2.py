import sys
sys.stdin = open("input.txt")
def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m

    left = merge_sort(m[:len(m) // 2])
    right = merge_sort(m[len(m) // 2:])

    left_len = len(left)
    right_len = len(right)
    result = [0] * (left_len+right_len)
    result_idx = 0
    left_idx = right_idx = 0
    if left[-1] > right[-1]:
        cnt += 1

    while left_idx < left_len or right_idx < right_len:
        if left_idx < left_len and right_idx < right_len:
            if left[left_idx] < right[right_idx]:
                result[result_idx] = left[left_idx]
                left_idx += 1
            else:
                result[result_idx] = right[right_idx]
                right_idx += 1
            result_idx += 1
        elif left_idx < left_len:
            for x in range(left_idx,left_len,1):
                result[result_idx] = left[x]
                result_idx += 1
            break
        elif right_idx < right_len:
            for x in range(right_idx,right_len,1):
                result[result_idx] = right[x]
                result_idx += 1
            break
    return result

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(maps)
    print("#{} {} {}".format(tc,ans[n//2],cnt))

# Pass