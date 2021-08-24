# Bitmask

> 비트단위 연산



* <<

  *  1 << n: 2n 즉, 원소가 n개일 경우의 모든 부분집합의 수

  

* &

  * i & (1<<j) : i의 j번째 비트가 1인지 확인

  

* 부분집합 생성하기

  ```python
  example = [3, 6, 7, 1, 5, 4]
  n = len(example)
  
  for i in range(1<<n):
    for j in range(n+1):
      if i & (1<<j):
        print(arr[j], end=", ")
        
  # example의 모든 부분집합이 출력
  ```

  

# Binary Search

> 중앙 값부터 검색, 정렬된 상태에서 사용가능



* Entire Code

```Python
def BinarySearch(example, key):
    start = 0
    end = len(example) - 1
    while start <= end:
        middle = (start + end) // 2
        if example[middle] == key:
            return True
        elif example[middle] > key:
            end = middle - 1
        elif example[middle] < key:
            start = middle + 1

    return False
```



