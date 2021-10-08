# 기웅님 코드

import sys
sys.stdin = open('sample_input.txt')

#lomuto partition
def partition(p, r):
    x = arr[r]              # 비교할 원소
    i = p-1                 # 시작 인덱스

    for j in range(p, r):
        if arr[j] <= x:     # 비교할 원소보다 작거나 같으면 i, j 같이 가다가
            i+=1            # 아닌 원소가 나오면 j만 이동하면서 다시 작은 원소가 나오면 걔랑 위치 바꿈
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]     # 피봇 위치를 정해줌
    return i+1

def quick_sort(l, r):
    if l<r:
        pivot = partition(l, r)
        quick_sort(l, pivot-1)
        quick_sort(pivot+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)

    print('#{} {}'.format(tc, arr[N//2]))