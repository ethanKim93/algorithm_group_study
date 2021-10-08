import sys
sys.stdin = open("input.txt")

# def quick_sort(li):
#     if len(li) <= 1:
#         return li
#
#     pivot = li[0]
#     remainder = li[1:]
#
#     left = [x for x in remainder if x <= pivot]
#     right = [x for x in remainder if x > pivot]
#
#     return quick_sort(left) + [pivot] + quick_sort(right)

# def quick_sort(li, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start+1
#     right = end
#     while left <= right:
#         while left <= end and li[left] <= li[pivot]:
#             left += 1
#         while right > start and li[right] > li[pivot]:
#             right -= 1
#
#         if left > right:
#             li[pivot], li[right] = li[right], li[pivot]
#         else:
#             li[left], li[right] = li[right], li[left]
#
#     quick_sort(li, start, right-1)
#     quick_sort(li, right+1, end)


def binary_search(li, l, r, goal, flag): # flag = 이번에 선택할 방향
    if l > r:
        return False

    mid = (l+r)//2
    if li[mid] == goal:
        return True

    if li[mid] < goal and 'right' in flag: # 찾고자 하는 값이 더 클 시
        return binary_search(li, mid+1, r, goal, ['left']) # 다음번엔 왼쪽에 있어야한다.

    elif li[mid] > goal and 'left' in flag: # 찾고자 하는 값이 더 작을 시
        return binary_search(li, l, mid-1, goal, ['right']) # 다음e번엔 오른쪽에 있어야한다.

    else:
        return False


t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    # A = quick_sort(list(map(int,input().split())))
    # A = list(map(int,input().split()))
    # quick_sort(A, 0, n-1)
    B = list(map(int,input().split()))
    ans = 0
    for i in B:
        if binary_search(A, 0, n-1, i, ['left', 'right']):
            ans += 1

    print("#{} {}".format(tc, ans))