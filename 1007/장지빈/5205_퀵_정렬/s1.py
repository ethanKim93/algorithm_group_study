import sys
sys.stdin = open('input.txt')

def partition(a, l, r):
    pivot = a[l]        # 피봇 설정(제일 왼쪽 값으로)
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= pivot:    # 피봇보다 큰 친구를 찾아 오른쪽으로
            i += 1
        while i <= j and a[j] >= pivot:     # 피봇보다 큰 친구를 찾아 왼왼으로
            j -= 1
        if i < j:                           # 교챠여부 판단
            a[i], a[j] = a[j], a[i]         # 교차하지 않았다면 두개 변경
    a[l], a[j] = a[j], a[l]
    return j

def quick_sort(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quick_sort(a, l, s-1)
        quick_sort(a, s+1, r)

for tc in range(1, int(input())+1):
    ans = 0
    N = int(input())
    li = list(map(int, input().split()))


    quick_sort(li, 0, N-1)
    ans = li[N//2]
    print('#{} {}'.format(tc, ans))


# def quick(start, end):
#     if end - start <= 1:
#         return
#
#     front = start
#     rear = front - 1
#     pivot = end - 1
#
#     while front < end:
#         if nums[front] <= nums[pivot]:
#             rear += 1
#             nums[rear], nums[front] = nums[front], nums[rear]
#
#         front += 1
#
#     quick(start, rear)  # 마지막 rear 기준 왼쪽
#     quick(rear + 1, end)  # 마지막 rear 기준 오른쪽
#
#
# for case in range(int(input())):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     quick(0, N)
#     print("#{} {}".format(case + 1, nums[N//2]))
