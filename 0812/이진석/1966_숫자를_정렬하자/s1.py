import sys

sys.stdin = open('input.txt')


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    prev_arr, next_arr = [], []
    for num in arr[1:]:
        if num < pivot:
            prev_arr.append(num)
        else:
            next_arr.append(num)

    return quick_sort(prev_arr) + [pivot] + quick_sort(next_arr)


for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = quick_sort(numbers)
    answer = ' '.join(map(str, numbers))
    print('#{} {}'.format(tc, answer))
