T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    '''
    버블 소트(오름차순)
    for i : N-1 > 1# 정렬구간의 끝 인덱스
        for j : 0-> i-1
            if arr[j]>arr[j+1]:
                arr[j] <-> arr[j+1]
    '''
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]: