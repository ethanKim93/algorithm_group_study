# 못풂

# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력

import sys
sys.stdin = open('sample_input.txt', 'r')

# 긁어옴
# 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고,
# 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량을 대폭 줄일 수 있습니다.
def sort(low, high):
    if high - low < 2:  # 요소 1개 남을 때까지 분할했을 때 return
        return
    mid = (low + high) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)

def merge(low, mid, high):
    temp = [0] * (high-low)
    l, h = low, mid
    i = 0

    global cnt
    if arr[mid-1] > arr[high-1]:
        cnt += 1

    while l < mid and h < high:
        if arr[l] < arr[h]:
            temp[i] = arr[l]
            i += 1
            l += 1
        else:
            temp[i] = arr[h]
            i += 1
            h += 1

    while l < mid:
        temp[i:] = arr[l:mid]
        i = high-low
        l += 1
    while h < high:
        temp[i:] = arr[mid:high]
        i = high - low
        h += 1

    for k in range(0, high-low):
        arr[k] = temp[k]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sort(0, len(arr))
    print('#{} {} {}'.format(tc, arr[N//2], cnt))


#############################################################################
## testcase 결과는 맞는데... 홈페이지에서 제한시간 초과
#
# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
# def merge(left, right):
#     global cnt
#     result = []
#
#     if left[-1] > right[-1]:
#         cnt += 1
#
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] < right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#
#         elif len(left) > 0:
#             result.extend(left)
#             left = []  # extend() 메서드는 pop과 달리 추가한 리스트를 그대로 놔둬서
#         elif len(right) > 0:
#             result.extend(right)
#             right = []
#     return result
#
#
# def merge_sort(m):
#     if len(m) == 1: return m
#
#     middle = len(m) // 2
#     left = m[:middle]
#     right = m[middle:]
#
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(left, right)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#     cnt = 0
#     print('#{} {} {}'.format(tc, merge_sort(ai)[N//2], cnt))