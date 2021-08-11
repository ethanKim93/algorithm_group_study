import sys
sys.stdin = open("input.txt")

T = int(input())

di = [0, 1, 0, -1] #오른쪽부터 시계방향 순
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())

    # NxN 0으로 채워진 배열
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    dir = 0 #이동방향
    i, j = 0, -1
    while cnt <=N*N: #쓸 값이 칸 수를 넘어가지 않았으면 반복
        ni, nj = i + di[dir], j + dj[dir] #이전칸으로부터 진행방향으로 이동한 칸 좌표
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: #영역 내부이고 아직 기록되지 않은 칸이면 꼭 뒤의 값이 뒤로 와야함
            arr[ni][nj] = cnt
            cnt += 1 #다음칸에 쓸 값
            i, j = ni, nj #현재칸을 다음칸 계산을 위한 값으로 사용
        else:
            dir = (dir + 1) % 4 #방향을 바꾸는 작업 => 0123 0123으로 하고싶은 거라서
            # 01234567이 정상일때 %4씩을 해주면 4는 다시 0이되고 123순으로 된다

    print('#{} '.format(tc))
    for i in range(N):
        print(*arr[i])