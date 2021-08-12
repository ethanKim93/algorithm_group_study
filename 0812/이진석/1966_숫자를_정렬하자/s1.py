import sys

sys.stdin = open('input.txt')


def quick_sort(arr):
    """
    quick sort : 기준점을 잡고 그 수보다 큰 배열, 작은 배열을 나누는 함수를 재귀형태로 해서 정렬
    """
    if len(arr) <= 1:  # 재귀 종료
        return arr
    pivot = arr[0]  # 기준점
    prev_arr, next_arr = [], []
    for num in arr[1:]: # 기준점 이후 인덱스의 값을 기준점보다 작은지 큰지 구분
        if num < pivot:
            prev_arr.append(num)
        else:
            next_arr.append(num)

    return quick_sort(prev_arr) + [pivot] + quick_sort(next_arr) # 작은수의 배열, 기준점, 큰 수의 배열


for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = quick_sort(numbers)
    answer = ' '.join(map(str, numbers))
    print('#{} {}'.format(tc, answer))
