# 선택 정렬 함수를 재귀 알고리즘으로 작성하기
# 선택 정렬 => 가장 작은 수의 인덱스를 찾아서 맨 앞부터 자리를 바꿈

def select_sort(i, N):
    if i == N:
        print(arr)
    else:
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        select_sort(i+1,N)

arr = [9, 7, 8, 3, 5, 2, 1, 10]
select_sort(0,len(arr))
