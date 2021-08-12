import sys
sys.stdin = open('input.txt')
from pprint import pprint

for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점의 column index 찾기
    for c in range(100):
        if arr[99][c] == 2:
            break
    # 도착지점에서 거꾸로 올라가기
    r = 99

    while r > 0:
        # 왼쪽 먼저 확인
        if (c - 1 >= 0) and arr[r][c - 1] == 1:
            arr[r][c] = -1  # 갔다가 다시 되돌아오는 것 방지
            c -= 1
        # 오른쪽 확인
        elif (c + 1 < 100) and arr[r][c + 1] == 1:
            arr[r][c] = -1
            c += 1
        else:
            r -= 1

    print('#{} {}'.format(tc, c))