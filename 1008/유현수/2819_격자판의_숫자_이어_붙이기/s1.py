import sys
sys.stdin = open('sample_input.txt')


def move(r, c, line, cnt):      # 시작 행 인덱스, 시작 열 인덱스, 움직이면서 만드는 수, 이동 횟수
    if cnt == 6:                # 이동 횟수가 끝났을 때
        if line not in ans:     # line이 처음 나온 수라면
            ans.append(line)    # ans에 추가
        return                  # 이동 횟수가 끝나면 함수 종료

    for d in range(4):                                  # 4방향 탐색
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:                 # 격자 범위 이내
            move(nr, nc, line+matrix[nr][nc], cnt+1)    # 이동


dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    matrix = [list(input().split()) for _ in range(4)]

    ans = []

    for i in range(4):
        for j in range(4):          # 격자판의 모든 지점에서 시작해본다.
            line = matrix[i][j]     # move 함수의 결과로 나오는 7자리 수를 line에 기록
            move(i, j, line, 0)

    print('#{} {}'.format(tc, len(ans)))