# 보충수업때 진행
import sys
sys.stdin = open('sample_input.txt')


def merge(left1, right1):
    global cnt

    left2, right2 = len(left1), len(right1)
    result = [0] * (left2 + right2)
    left3, right3 = 0, 0
    i = 0

    if left1[-1] > right1[-1]:
        cnt += 1

    while left3 != left2 and right3 != right2:
        if left1[left3] <= right1[right3]:
            result[i] += left1[left3]
            i += 1
            left3 += 1
        else:
            result[i] += right1[right3]
            i += 1
            right3 += 1

    if left3 != left2:
        while left3 != left2:
            result[i] += left1[left3]
            i += 1
            left3 += 1

    if right3 != right2:
        while right3 != right2:
            result[i] += right1[right3]
            i += 1
            right3 += 1

    return result


def merge_sort(Data):
    if len(Data) <= 1:
        return Data

    mid = len(Data) // 2
    left1 = merge_sort(Data[:mid])
    right1 = merge_sort(Data[mid:])
    return merge(left1, right1)


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = list(map(int, input().split()))
    cnt = 0
    Data = merge_sort(Data)

    print('#{} {} {}'.format(tc, Data[N//2], cnt))