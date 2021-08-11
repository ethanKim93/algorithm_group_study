import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0

    for x in range(len(arr)):
        for y in range(len(arr[x])):
            for mode in range(4):
                pointX = x + dx[mode]
                pointY = y + dy[mode]
                if 0 <= pointX < n and 0 <= pointY < n:
                    result += abs(arr[pointX][pointY] - arr[x][y])
    print(result)




