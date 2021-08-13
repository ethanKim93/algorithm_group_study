import sys
sys.stdin = open("input.txt")

# 색칠하기
def coloring(idx1, idy1, idx2, idy2, color):
    global maps
    for i in range(idx1, idx2+1):
        for x in range(idy1, idy2+1):
            maps[i][x] += color # 조건: 같은 색은 겹치지 않는다


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ans = 0
    maps = [[0]*10 for _ in range(10)]
    for i in range(n):
        idx1, idy1, idx2, idy2, color = map(int, input().split())
        coloring(idx1, idy1, idx2, idy2, color)

    for i in range(10):
        for x in range(10):
            if maps[i][x] >= 3: # 빨간색과 파란색이 겹쳤으면 count
                ans += 1

    print("#{} {}".format(tc, ans))