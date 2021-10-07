import sys
sys.stdin = open("input.txt")

def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    r, l = 0, 0
    while len(left)>l or len(right)>r:
        if len(left)>l and len(right)>r:
            if left[l] <= right[r]:
                # result.append(left.pop(0))
                result += [left[l]]
                l += 1
            else:
                # result.append(right.pop(0))
                result += [right[r]]
                r += 1
        elif len(left) > l:
            # result.append(left.pop(0))
            result += [left[l]]
            l += 1
        elif len(right) > r:
            # result.append(right.pop(0))
            result += [right[r]]
            r += 1
    return result

def devide(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = devide(left)
    right = devide(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
    arr = devide(ai)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))