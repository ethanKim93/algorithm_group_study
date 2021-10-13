import sys
sys.stdin = open('sample_input.txt')

def cafe_tour(i, j, k):
    global ans
    if (k == 3) and (cafe[i][j] in visited):
        if len(visited) > ans:
            ans = len(visited)
        return

    # \아래  /아래  \위  /위
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    ni = i + di[k]
    nj = j + dj[k]

    if 0 <= ni < N and 0 <= nj < N and cafe[ni][nj] not in visited:
        visited.append(cafe[i][j])
        cafe_tour(ni, nj, k)
        cafe_tour(ni, nj, k+1)

    else:
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(0, N-2):
        for j in range(1, N-1):
            if (cafe[i+1][j-1] != cafe[i][j]) and (cafe[i+1][j+1] != cafe[i][j]) and (cafe[i+1][j-1] != cafe[i+1][j+1]):
                visited = []
                cafe_tour(i, j, 0)

    print(ans)