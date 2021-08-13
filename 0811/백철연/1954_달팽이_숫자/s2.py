import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1] #오른쪽부터 시계방향 순
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    #NxN 0으로 채워진 배열
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    dir = 0 # 이동방향
    i, j = 0, -1
    while cnt <= N*N: # 쓸 값이 칸 수를 넘어가지 않았으면 반복
        ni, nj = i + di[dir], j + dj[dir] # 이전칸으로 부터 진행방향으로 이동한 칸 좌표
        if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0: # 영역 내부이고 아직 기록되지 않은 칸이면
            arr[ni][nj] = cnt
            cnt += 1 # 다음칸에 쓸 값
            i, j = ni, nj # 현재칸을 다음칸 계산을 위한 값으로 사용
        else:
            dir = (dir + 1) % 4

    print('#{} {}'.format(tc,arr))
        # for i in range(N):
        #     for j in range(N):
        #         print(arr[i][j], end= ' ')
        #     print()

    # for i in range(N):
    #     print(*arr[i]) # *arr 일차원배열을 하나씩 꺼내서 순서대로 찍어줌


