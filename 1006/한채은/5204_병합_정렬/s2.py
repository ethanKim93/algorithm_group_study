import sys
sys.stdin=open('sample_input.txt')

def merge(left, right):
    lp = rp = 0
    res = []
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            res.append(left[lp])
            lp += 1
        else:
            res.append(right[rp])
            rp += 1

    # 남은 것을 res의 뒤에 복사
    res += left[lp:]
    res += right[rp:]

    # if lp < len(left):
    #     res += left[lp]
    # if rp < len(right):
    #     res += right[rp:]

    return res

def mergesort(lst):
    global cnt

    if len(lst) == 1:
        return lst

    m = len(lst) // 2
    left = mergesort(lst[:m])
    right = mergesort(lst[m:])

    if left[-1] > right[-1]:
        cnt += 1

    res = merge(left, right)
    return res


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = mergesort(arr)

    print('#{} {} {}'.format(tc, arr[N//2], cnt))
