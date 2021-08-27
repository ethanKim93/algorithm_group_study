import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    color = []

    for n in range(N):
        a = [flag[n].count('W'), flag[n].count('B'), flag[n].count('R')]
        color.append(a)

    b_width = 1     # blue 색상 넓이 1 ~ N-2

    total = []
    while b_width <= N-2:
        b_start = 1  # blue 색상 시작 위치
        while b_start <= (N-1-b_width):
            way = [0] * 3
            for w in range(b_start):
                way[0] += color[w][1] + color[w][2]
            for b in range(b_start, b_start + b_width):
                way[1] += color[b][0] + color[b][2]
            for r in range(b_start+b_width, N):
                way[2] += color[r][0] + color[r][1]
            total.append(sum(way))
            b_start += 1
        b_width += 1


    print('#{} {}'.format(tc, min(total)))

