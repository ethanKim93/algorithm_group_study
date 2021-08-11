import sys
sys.stdin = open('input.txt')
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    dx = [0, 1, 0, -1] # 우, 좌
    dy = [1, 0, -1, 0] # 상, 하
    for i in range(N):      #배열 수 만큼 x축 순회
        for j in range(N):  #배열 수 만큼 y축 순회
            sum_abs = 0
            for k in range(len(dx)):        # 델타 상하좌우 이동 가능한 좌표만큼 range 설정
                newi = i + dx[k]
                newj = j + dy[k]
                if 0 <= newi < N and 0 <= newj < N:     #새로 설정한 좌표가 음수라면 실행하지 않고 다시 반복문으로
                    value_abs = li[newi][newj] - li[i][j]   #새로 설정한 좌표가 양수라면 실행
                    if value_abs >= 0:
                        sum_abs += value_abs
                    else:
                        sum_abs -= value_abs
            total += sum_abs
    print('#{} {}'.format(tc, total))