import sys
sys.stdin = open('sample_input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
def make_num(r, c, num, cnt):
    '''
    r, c : 좌표
    num : 현재까지의 숫자
    cnt : 이동횟수
    '''
    if cnt == 7:
        answer.add(num)
        return

    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            make_num(nr, nc, num*10+table[nr][nc], cnt+1)
    return
for tc in range(1, int(input())+1):
    table = [list(map(int, input().split())) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]
    answer = set()
    for i in range(4):
        for j in range(4):
            make_num(i, j, table[i][j], 1)
    print('#{} {}'.format(tc, len(answer)))