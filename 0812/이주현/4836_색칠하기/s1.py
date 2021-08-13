import sys
sys.stdin = open('sample_input.txt')

def painting(paper, start, end, color):
    purple = 0
    # 지정된 구역을 작업
    for row in range(start[0], end[0]+1):
        for col in range(start[1], end[1]+1):
            # 색상이 다르다 -> 0인 부분이 채워지거나 보라색이 된다.
            if paper[row][col] != color:
                paper[row][col] += color
            if paper[row][col] == 3:
                purple += 1

    return purple

T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    paper = [[0] * 10 for _ in range(10)]
    count = 0

    for idx in range(N):
        start = tuple(area[idx][0:2])                   # 시작점
        end = tuple(area[idx][2:4])                     # 끝점
        color = area[idx][-1]                           # 색상
        count += painting(paper, start, end, color)     # 작업

    print("#{} {}".format(test_case, count))