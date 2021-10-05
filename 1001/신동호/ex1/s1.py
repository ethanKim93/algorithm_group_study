A = [8, 6, 3, 4, 5, 1, 2, 7]

def SelectionSort(i):
    n = len(A)
    if i == n: # basis case
        return
    minI = i # i가 최소값의 위치라 가정
    for j in range(i+1, n): # i 이후의 원소들에 대해 최소값 비교
        if A[j] < A[minI]:
            minI = j
    A[minI], A[i] = A[i], A[minI] # 최소값 인덱스 변경
    SelectionSort(i+1) # 크기 1씩 줄여가며 재귀

SelectionSort(0)
print(A)

