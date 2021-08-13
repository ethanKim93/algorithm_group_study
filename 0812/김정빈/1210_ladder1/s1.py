import sys
sys.stdin = open("input.txt")

d = [(-1, 0),(0, -1),(0, 1)] # 상 좌 우

# for tc in range(1, 11):
for tc in range(1):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    where2 = arr[99].index(2) #2가 있는 자리 찾기
    r, c = 98, where2 #행, 열 초기값
    dir = 0 #이동방향
    ans = 0 #사다리 시작한 위치(결과)

    while r > 0:
        y, x = r + d[dir][0], c + d[dir][1]
        if arr[y][x-1] == 0 and arr[y][x+1] == 0:
            r -= 1
            print(arr[y][x])
            # if 0 <= y < 100 and 0 <= x < 100:#범위 안이고