import sys
sys.stdin = open("sample_input.txt")
def partition(arr, l, r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    quickSort(ai, 0, N-1)
    print('#{} {}'.format(tc, ai[N//2]))

# 최종코드
def partition(A, p, r):  # A: 정렬할 배열 / p: 배열의 첫번째 인덱스 / r: 배열의 마지막 인덱스
    x = A[r]  # pivot 값, 배열의 맨 마지막 요소
    i = p-1  # 배열의 한 칸 전에서 시작
    for j in range(p, r):  # 배열 처음부터 r-1까지 이동
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i], A[r] = A[r], A[i]
    return i


def qsort(A, p, r):
    if p < r:  # 이 조건 들어가야 maximum recursion 오류 안뜸
        s = partition(A, p, r)
        qsort(A, p, s - 1)
        qsort(A, s + 1, r)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    qsort(ai, 0, len(ai)-1)
    print('#{} {}'.format(tc, ai[N//2]))