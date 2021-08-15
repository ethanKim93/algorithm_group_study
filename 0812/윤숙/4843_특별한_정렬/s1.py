import sys
sys.stdin=open('sample_input.txt')
T=int(input())

for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int, input().split()))

    M=10
    for n in range(N - 1, 0, -1):
        for j in range(0, n):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



    for i in range(0, N-1,2):
        max=i
        for j in range(i+1, N):
            if arr[max] < arr[j]:
                max =j

            arr[i], arr[max] = arr[max], arr[i]

    arr_result=[]
    for K in range(M):
        arr_result.append(arr[K])


    result = " ".join(map(str, arr_result))
    print('#{} {}'.format(tc,result))
