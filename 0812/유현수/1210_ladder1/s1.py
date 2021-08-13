import sys
sys.stdin=open('input.txt')

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]

    # 도착지 인덱스 찾기
    r = 99
    c = 0
    for i in range(100):
        if ladder[99][i] == 2:
            c = i

    while r > 0:
        if not c:                   # c가 0일때는 오른쪽만 검사
            if ladder[r][c+1]:      # 검사해서 값이 1이면
                ladder[r][c] = 0    # 현재 위치를 0으로 변경하고(다시 돌아오지 않도록)
                c += 1              # 오른쪽으로 이동
            else:
                r -= 1
        elif c == 99:               # c가 99일때는 왼쪽만 검사
            if ladder[r][c-1]:
                ladder[r][c] = 0
                c -= 1
            else:
                r -= 1
        else:                       # 그 외에는 양쪽 다 검사
            if ladder[r][c-1]:
                ladder[r][c] = 0
                c -= 1
            elif ladder[r][c+1]:
                ladder[r][c] = 0
                c += 1
            else:
                r -= 1

    print('#{} {}'.format(T, c))