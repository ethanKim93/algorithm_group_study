import sys
sys.stdin = open('input.txt')

T = int(input())
cnt = 0

def sort1(x):
    for i in range(len(x)):
       min1 = i
       for j in range(i+1, len(x)):
           if arr[j][1] < arr[min1][1]:
               min1 = j
       arr[i], arr[min1] = arr[min1], arr[i]

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))


    while arr:
        sort1(arr)
        a = arr.pop(0)
        cnt += 1
        for i in range(len(arr)):
            if a[1] <= arr[i][0]:
                arr = []


    print(cnt)