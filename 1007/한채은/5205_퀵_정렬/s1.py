# 피봇을 기준으로 큰 숫자와 작은 숫자를 교환한 다음 배열을 반으로 나눔
# 피봇보다 작은 숫자는 왼쪽, 큰 숫자는 오른쪽
import sys
sys.stdin = open('sample_input.txt')

def quicksort(left, right):
    if left >= right:
        return

    # 분할할 리스트의 0번째를 pivot으로 설정(제일 왼쪽)
    pivot = left
    # pivot 다음 요소인 1번째 요소
    i = left+1
    # 마지막 요소에서 거꾸로 가면서 pivot보다 작은지 큰지 비교
    j = right-1

    while i <= j:
        while i <= j and arr[pivot] >= arr[i]:
            i += 1

        while i <= j and arr[pivot] <= arr[j]:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[pivot], arr[j] = arr[j], arr[pivot]

    # left < right가 될때까지 함수를 나눠서 계속해서 재귀호출
    quicksort(left, j)
    quicksort(j+1, right)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    left = 0
    right = len(arr)
    quicksort(left, right)

    result = arr[N//2]
    print('#{} {}'.format(tc, result))