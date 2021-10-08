import sys

sys.stdin = open('input.txt')


def quicksort(l, r):
    global arr
    if l < r:
        s = partition(l, r)
        quicksort(l, s - 1)  # smaller
        quicksort(s + 1, r)  # bigger


def partition(l, r):
    global arr
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= p:
            # 피봇과 비교해서 피봇보다 작은값이면 인덱스 증가
            # 피봇보다 인덱스는 큰값을 만나면 멈춤
            i += 1
        while i <= j and arr[j] >= p:
            # 피봇과 비교해서 피봇보다 큰값이면 인덱스 증가
            # 피봇보다 인덱스는 작은값을 만나면 멈춤
            j -= 1
        if i < j:
            # i,j 인덱스기준으로 큰값과 작은값 인덱스로 값을 스왑
            arr[i], arr[j] = arr[j], arr[i]

    # i와 j의의 인덱스가 i>j가 되면 반복문 루프를 빠져나오게 되고
    # j가 가르키는 값은 분할해서 나눈 뒷부분의 첫번째 방 인덱스가 된다.
    arr[l], arr[j] = arr[j], arr[l]

    return j

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    l = 0
    r = len(arr)
    quicksort(l, r - 1)
    print('#{} {}'.format(tc,arr[N // 2]))
