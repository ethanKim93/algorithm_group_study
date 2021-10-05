# 선택 정렬 함수(SelectionSort)를 재귀적 알고리즘으로 작성해 보시오.

def SelectionSort(lst, start, N):
    if N == 1:
        return
    mini = lst.pop(lst.index(min(lst[start:])))
    lst.insert(start, mini)
    SelectionSort(lst, start+1, N-1)
    return lst

lst=[1, 3, 0, 2, 4, 7, 5]
print(SelectionSort(lst, 0, len(lst)))


