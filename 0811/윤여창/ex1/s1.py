import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    total_1 = 0
    total_2 = 0


    for x in range(len(li)):
        for y in range(len(li[x])):
            for i in range(4):
                test_x = x + dx[i]
                test_y = y + dy[i]
                if 0 <= test_x < len(li) and 0 <= test_y < len(li[x]):
                    total_1 = abs(li[test_x][test_y] - li[x][y])
                    total_2 += total_1
    print(total_2)