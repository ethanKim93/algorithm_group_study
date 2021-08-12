import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 2D transpose
    puzzle_tr = map(list, zip(*puzzle))
    # 패딩영역 추가
    puzzle = [[0]+x+[0] for x in puzzle]
    puzzle_tr = [[0]+x+[0] for x in puzzle_tr]

    cnt = 0
    # j, i 방향 검사
    for i in range(N):
        for j in range(N-K+3):
            if puzzle[i][j:j+K+2] == [0]+[1]*K+[0]:
                cnt += 1
            if puzzle_tr[i][j:j+K+2] == [0]+[1]*K+[0]:
                cnt += 1

    print('# {} {}'.format(tc, cnt))