import sys

sys.stdin = open('input.txt')

# 0822 재풀이
for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(1,len(arr)):

        for j in range(i,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            print(arr)
