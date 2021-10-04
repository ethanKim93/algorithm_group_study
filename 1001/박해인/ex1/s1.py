# 연습문제 1 선택 정렬 함수를 재귀적 알고리즘으로 작성해 보시오.
# [62,98,54,23,14,94,56] -> [14, 23, 54, 56, 62, 94, 98]

def selectionSort(a, s):
    n = len(a)
    if s == n-1:  # 정렬의 시작점과 끝-1점이 일치한다면 (마지막 2개가 남았을 때까지 해도 정렬이 되므로)
        return  # 정렬 종료
    min_i = s  # 시작점을 가장 작다고 가정
    for i in range(s+1, n):  # 시작점+1 부터 끝까지 탐색하면서 작은 i 찾기
        if a[min_i] > a[i]:  # 최소값이라고 가정한 것보다 i가 더 작다면
            min_i = i  # i가 최소
    a[s], a[min_i] = a[min_i], a[s]  # s와 새로 찾은 가장 작은 값 바꾸기
    selectionSort(a, s+1)  # 정렬된 a로 다음줄부터 다시 탐색

numbers = [62,98,54,23,14,94,56]
selectionSort(numbers, 0)
print(numbers)