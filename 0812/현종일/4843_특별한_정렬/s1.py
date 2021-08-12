import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def min_sort(a, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_sort(arr, N)
    print(arr)

    new_arr = []

    for i in range(1, len(arr)+1):
        if i % 2:
            new_arr.append(arr[-(i//2+1)])
        else:
            new_arr.append(arr[i//2-1])
    new_arr = new_arr[:10]

    print('#{}'.format(tc), end=' ')
    print(*new_arr)



