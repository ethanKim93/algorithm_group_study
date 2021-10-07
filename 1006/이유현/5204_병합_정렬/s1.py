import sys
sys.stdin = open('sample_input.txt')


def merge_sort(numbers):
    global cnt

    n = len(numbers)
    if n <= 1:
        return

    mid = n // 2
    left_group = numbers[:mid]
    right_group = numbers[mid:]

    merge_sort(left_group)
    merge_sort(right_group)

    if left_group[-1] > right_group[-1]:
        cnt += 1

    left = right = now = 0

    while left < len(left_group) and right < len(right_group):
        if left_group[left] < right_group[right]:
            numbers[now] = left_group[left]
            left += 1
            now += 1
        else:
            numbers[now] = right_group[right]
            right += 1
            now += 1
    while left < len(left_group):
        numbers[now] = left_group[left]
        left += 1
        now += 1

    while right < len(right_group):
        numbers[now] = right_group[right]
        right += 1
        now += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))