import sys
sys.stdin = open('sample_input.txt')


def bfs(end):
    cnt = 0
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]   # 상 하 좌 우
    while end:    # end 값이 존재하면 계속 진행
        empty_lst = []
        while end:
            x, y = end.pop()
            for k, l in move:
                dx = x + l
                dy = y + k
                if 0 <= dx < N and 0 <= dy < N:  # 맵 범위 내에 있을때
                    if map_lst[dx][dy] == 3:    # 출발지 3에 도달하면 이동하면서 쌓인 cnt 값을 리턴
                        return cnt
                    if not map_lst[dx][dy]:     # 안지나간 통로(0)라면 1로 변경한 후 lst에 추가
                        map_lst[dx][dy] = 1
                        empty_lst.append((dx, dy))
        cnt += 1
        end = empty_lst
    return 0    # 출발지를 발견할 수 없으면 0 반환


for t in range(1, 1 + int(input())):
    N = int(input())
    map_lst = []
    for _ in range(N):
        map_lst.append(list(map(int, list(input()))))
    end = []
    for i in range(N):
        for j in range(N):
            if map_lst[i][j] == 2:  # 도착지 2에 도달하면 end에 해당 값을 넣고 break
                end.append((i, j))
                break
        else:
            continue
        break
    print('#{} {}'.format(t, bfs(end)))