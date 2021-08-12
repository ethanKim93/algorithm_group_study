import sys
sys.stdin = open('sample_input.txt')

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    print(selection_sort(arr))
    for i in range(1, len(arr)//2):