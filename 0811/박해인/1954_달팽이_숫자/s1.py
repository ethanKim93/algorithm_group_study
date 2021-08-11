import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1] # 우, 하, 좌, 상
dj = [1, 0, -1, 0]

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # NxN 0으로 채워진 배열
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    dir = 0  # 이동방향 direction
    i, j = 0, -1  # 0, -1이라는 가상의 칸에서 시작

    while cnt <= N*N:   # count가 쓸 값이 칸 수를 넘어가지 않았으면 반복
        ni, nj = i + di[dir], j + dj[dir]  # 이 전칸으로부터 진행방향으로 이동한 칸
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:  # 영역 내부이고 아직 기록되지 않은 칸이면
            arr[ni][nj] = cnt
            cnt += 1  # 다음칸에 쓸 값
            i, j = ni, nj  # 현재 칸을 다음 칸 계산을 위한 값으로 변경
        else:
            dir = (dir + 1) % 4  # direction을 0, 1, 2, 3에서 순회할 수 있도록

    print('#{}'.format(test_case))

    for i in range(N):
        print(*arr[i])  # 1차원 배열에 있는 요소를 꺼내서 하나씩 출력해준다.