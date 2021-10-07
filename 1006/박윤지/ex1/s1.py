# 연습문제1
# 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오
# Hoare-Partition 알고리즘

def partition(arr, l, r):  # arr: 정렬할 배열 / l: 배열 첫 인덱스 / r: 배열 마지막 인덱스
    p = arr[l]  # 피봇 값을 배열의 맨 처음 값으로 설정 ( Hoare-Partition 알고리즘 특징 )
    i = l  # i는 배열 맨 왼쪽에서부터 오른쪽으로 이동
    j = r  # j는 배열 맨 오른쪽에서부터 왼쪽으로 이동
    while i <= j:
        while i <= j and arr[i] <= p:  # arr[i]가 피봇 값보다 큰 값을 만날 때까지 계속 i++ / i < j 하면 크로스가 안되어 while문 무한루프됨
            i += 1
        while i <= j and arr[j] >= p:  # arr[j]가 피봇 값보다 작은 값을 만날 때까지 계속 j++
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def quickSort(arr, l, r):  # arr: 정렬할 배열 / l: 배열 첫 인덱스 / r: 배열 마지막 인덱스
    if l < r:
        s = partition(arr, l, r)
        quickSort(arr, l, s-1)
        quickSort(arr, s+1, r)


# ex1 = [11, 45, 23, 81, 28, 34]
# ex1 = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
ex1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
quickSort(ex1, 0, len(ex1)-1)
print(ex1)

