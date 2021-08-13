import sys
sys.stdin = open('sample_input.txt')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10):
        if not i % 2: # 짝수 인덱스일경우 최대값
            max_i = i
            for j in range(i+1, len(arr)):
                if arr[max_i] < arr[j]:
                    max_i = j
            arr[i], arr[max_i] = arr[max_i], arr[i]
        else:  # 홀수 인덱스일 경우 최소값
            min_i =i
            for j in range(i+1, len(arr)):
                if arr[min_i] > arr[j]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]
    res_arr = arr[:10]

    print('#{} {}'.format(tc, *res_arr))
