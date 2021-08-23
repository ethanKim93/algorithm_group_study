import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        cnt1 = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            else:
                cnt1 += 1
        if cnt1 == K:
            result += 1

    for j in range(N):
        cnt1 = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt1 == K:
                    result += 1
                cnt1 = 0
            else:
                cnt1 += 1
        if cnt1 == K:
            result += 1

    print('#{} {}'.format(tc, result))



'''
(1) 가로검사 세로검사후 빈칸이면 카운트, 벽을 만나면 지금까지 세왔던 카운트가 K와 같으면 +1, 아니라면 0으로 초기화한 후 넘어간다
1) 벽으로 바꼈을때 2) 끝까지 갔을때
(2) 가로 검사한후 90도 회전한 모양에서 다시 가로 검사
(3) 오른쪽과 아래에 벽을 만들어 두면 조건이 하나 줄어듬(끝으로 갔을때 고려X)
'''