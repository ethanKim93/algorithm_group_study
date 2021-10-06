def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m

    left = merge_sort(m[:len(m) // 2])
    right = merge_sort(m[len(m) // 2:])

    if left[-1] > right[-1]:
        cnt += 1
    result = []
    while left or right:
        if left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result = result + left
            left = []
        elif right:
            result = result + right
            right = []

    return result

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    maps = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(maps)
    print("#{} {} {}".format(tc,ans[n//2],cnt))
# Fail: Time over