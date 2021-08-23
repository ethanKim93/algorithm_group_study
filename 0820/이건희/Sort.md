# Sort

> 교수님께서 시험에 나온다고 하셔서 정리

------------

### Bubble Sort

> O(n2)

* 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동

  ```python
  if example[i] > example[i+1]:
  	example[i], example[i+1] = example[i+1], example[i]
  ```

  

* 한 단계가 끝나면 가장 큰 원소가 마지막 자리

  ```python
  mx = example[-1]
  ```



* Entire code

  ```python
  def BubbleSort(example):
    for i in range(len(exmaple)-1, 0, -1): # 마지막 인덱스부터 1번째 항까지 '거꾸로'
      for x in range(0,i): # 정렬이 '끝'부터 완료되니까 범위를 하나씩 줄여가면서
        if example[x] > example[x+1]:
          example[x], example[x+1] = example[x+1], example[x]
          
  ```



----------

### Counting Sort

> O(n+k)

#### 1. 원소의 갯수를 counts의 원소로 조정

![스크린샷 2021-08-20 오후 5.22.26](Sort.assets/스크린샷 2021-08-20 오후 5.22.26.png)



#### 2. 각 index 까지의 총 합으로 index를 변경

![스크린샷 2021-08-20 오후 5.26.21](Sort.assets/스크린샷 2021-08-20 오후 5.26.21.png)



#### 3. 위치를 기록할 Temp 생성 및 첫번째 작업 시작(TEMP그림이 index 1부터 시작하는듯)

![스크린샷 2021-08-20 오후 5.27.45](Sort.assets/스크린샷 2021-08-20 오후 5.27.45.png)

* DATA의 마지막 인덱스가 1이므로, counts에서 1에 해당하는 값인 4를 1만큼 감소
* Temp의 4번째 항목에 1을 기입



#### 4. DATA는 거꾸로 index를 돌고 counts에서 해당하는 값을 찾아 Temp에 기록

![스크린샷 2021-08-20 오후 5.32.40](Sort.assets/스크린샷 2021-08-20 오후 5.32.40.png)

* 이런 식으로 DATA[0]까지 반복



#### 5. 최종본

![스크린샷 2021-08-20 오후 5.33.36](Sort.assets/스크린샷 2021-08-20 오후 5.33.36.png)



* Entire Code

```python
def Counting_Sort(data, counts, temp):
  counts = [0]*len(data)
  temp = [0]*len(data)
  
  for i in range(len(data)): # data 돌면서 count의 해당하는 위치에 ++1
    counts[data[i]] += 1
  
  for i in range(1, len(counts)): # count 돌면서 인덱스까지의 총합으로 바꿔주기
    counts[i] += counts[i-1]
 	
  for i in range(len(data)-1, -1, -1): # data의 모든 항목을 거꾸로 돌면서
    temp[counts[data[i]]] = data[i] # data의 항목에 해당하는 counts의 항목을 찾고 해당 값의 temp에 data의 인덱스를 넣어주기
    counts[data[i]] -= 1 # temp에 넣어줬으므로 counts의 해당 항목은 1--
    
  # 완료하면 temp = Sorted_list
```



-------------

### Selection Sort

> O(n2), 가장 작은 index를 골라서 앞으로!



* 주어진 리스트 중에서 최소값을 찾는다
* 그 값을 리스트의 맨 앞에 위치한 값과 교환
* Search 구역을 앞에서부터 하나씩 배제하며 반복



* Entire code

```Python
def Selection_Sort(data):
  for i in range(len(data)-1): # 마지막이 아닌 마지막 '전' 인덱스까지 탐색
    mn = i
    for x in range(i+1, len(a)): # 현재 위치 다음부터 끝까지 최소 값인 인덱스를 찾아 탐색
      if a[mn] > a[x]:
        mn = x
    a[i], a[mn] = a[mn], a[i] # 현재 위치와 최소 값을 교체
```


