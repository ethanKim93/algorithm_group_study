# 시간초과 (pop, append)
import sys
sys.stdin = open("input.txt")

def devide(arr):
    if len(arr) == 1:
        return arr
    left, right = [], []
    mid = len(arr)//2
    for x in range(0,mid):
        left.append(arr[x])
    for y in range(mid, len(arr)):
        right.append(arr[y])

    left = devide(left)
    right = devide(right)

    return merge(left, right)

def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
    arr = devide(ai)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))