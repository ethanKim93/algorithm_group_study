import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for row in range(N):
        for col in range(len(arr[row])):
            for idx in range(4):
                x = row + dx[idx]
                y = col + dy[idx]
                if (x>=0 and x<N) and (y>=0 and y<N):
                    tmp = arr[row][col] - arr[x][y]
                    if tmp < 0:
                        result -= tmp
                    else:
                        result += tmp

    print(result)