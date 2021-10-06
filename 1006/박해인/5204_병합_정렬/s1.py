import sys
sys.stdin = open('sample_input.txt')

def merge(left, right):
    result = []
    lp, rp = 0, 0
    global cnt

    while lp < len(left) and rp < len(right):
        if left[lp] <= right[rp]:
            result.append(left[lp])
            lp += 1
        else:
            result.append(right[rp])
            rp += 1

    result += left[lp:]
    result += right[rp:]

    return result


def merge_sort(m):
    global cnt

    if len(m) == 1:
        return m

    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])

    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())  # 정수의 개수 N
    data = list(map(int, input().split()))

    cnt = 0
    result_list = merge_sort(data)

    print('#{} {} {}'.format(test_case, result_list[N//2], cnt))