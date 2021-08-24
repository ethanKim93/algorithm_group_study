#1. 집합 [1, 2, 3]의 모든 부분집합 구하기

arr = [1, 2, 3]   # 구하고자 하는 부분 집합
N = len(arr)      # arr의 길이
sel = [0] * N     # a 리스트 (내가 해당 원소를 뽑았는지 체크하는 리스트)

def powerset(idx):
    if idx == N:                            # idx가 N과 같아지면
        for index, i in enumerate(sel):     # 인덱스(index)와 함께 반복 돌면서
            if i:                           # 원소를 선택한 경우(i == 1)
                print(arr[index], end=' ')  # 해당 인덱스(index)의 원소를 출력한다
        print()
        return
    sel[idx] = 1                            # sel의 idx번째 자리를 1로 바꾸고(사용하고)
    powerset(idx+1)                         # idx+1 을 인자로 넣어서 powerset 재귀 호출
    sel[idx] = 0                            # 사용한 경우를 위에서 확인했으니 이번엔 idx 자리의 원소를 뽑지 않은 상태로 바꾸고
    powerset(idx+1)                         # idx+1 을 인자로 넣어서 powerset 재귀 호출
                                            # 더 수행 할 코드가 없으면 해당 함수를 호출한 곳으로 돌아간다
powerset(0)



#2. 부분집합의 요소 중 합이 10이되는 것을 구하기

data = range(1, 11)
sel = [0] * len(data)

def powerset(idx):
    if idx < len(data):                                     # 부분집합을 찾아보자 (위에서와 반대로 조건분기)
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    else:
        total = 0
        for i in range(len(data)):
            if sel[i]:                                      # 1로 표시되어 있다면
                total += data[i]                            # total에 그 값을 더한다
        if total == 10:                                     # 반복이 다 끝나고 부분집합의 합이 10이 된다면
            for idx, num in enumerate(sel, start=1):        # 각 원소를 출력
                if num == 1:
                    print(idx, end=' ')
            print()
        return

powerset(0)



# 가지치기

data = range(1, 11)
sel = [0] * len(data)

def powerset(idx, subsum):
    if subsum == 10:
        for i in range(idx):                # idx 범위까지만 반복을 수행하면 된다
            if sel[i]:
                print(data[i], end=' ')
        print()
        return
    
    if idx < 10 and subsum < 11:            # idx 는 10 미만이면서 subsum(부분집합 중간합)도 10을 넘지 않는 경우에만 수행
        sel[idx] = 1
        # subsum += data[idx]
        powerset(idx+1, subsum+data[idx])   # 함수 호출시 인자에만 값을 더해주면 나중에 다시 빼주지 않아도 된다.
        sel[idx] = 0
        # subsum -= data[idx]
        powerset(idx+1, subsum)

powerset(0, 0)