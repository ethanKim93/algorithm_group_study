import sys

sys.stdin = open('input.txt')


def selection_sort(arr):  # 선택정렬
    """
    선택정렬 : 최소값을 차례대로 선택하여 0부터 위치를 교환하는 정렬방식
    """
    for i in range(len(arr)):
        min_idx = i
        min_num = arr[i]
        for j in range(i, len(arr)):
            if min_num > arr[j]:
                min_num = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = selection_sort(numbers)
    answer = ' '.join(map(str, numbers))
    print('#{} {}'.format(tc, answer))
