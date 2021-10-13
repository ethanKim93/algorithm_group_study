import sys

sys.stdin = open('sample_input.txt')

delta = [(-1, 1), (1, 1), (1, -1), (-1, -1)]  # 1시, 5시, 7시, 11시

def search(r, c, start, dir):
    global max_visit
    if dir == 3 and (r, c) == start:    # 사각형이 완성되었으며(네 방향 모두 진행), 출발지에 다시 돌아왔을 때
        if sum(visited) > max_visit:    # 방문한 카페 수 최댓값과 비교해서 최댓값 갱신
            max_visit = sum(visited)
            return

    if r < 0 or r >= N or c < 0 or c >= N or visited[cafe[r][c]]:   # 인덱스 유효성검사, 카페 방문+디저트 수 중복 여부 검사
        return

    visited[cafe[r][c]] = 1                                         # 방문 기록
    nr, nc = r + delta[dir % 4][0], c + delta[dir % 4][1]           # 동일한 방향으로 진행
    search(nr, nc, start, dir)
    if dir != 3:                                                    # 아직 갈 수 있는 방향이 있다면
        nr, nc = r + delta[(dir+1) % 4][0], c + delta[(dir+1) % 4][1]   # 다음 방향으로 진행
        search(nr, nc, start, dir+1)
    visited[cafe[r][c]] = 0                                         # 방문 기록 초기화

for tc in range(1, int(input()) + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    max_visit = -1                  # 최대 방문 가능한 카페
    visited = [0] * 101             # 방문한 카페의 디저트 가짓수를 인덱스로 방문여부 + 중복여부 체크
    for i in range(1, N - 1):
        for j in range(N - 2):
            search(i, j, (i, j), 0)
    print('#{} {}'.format(tc, max_visit))