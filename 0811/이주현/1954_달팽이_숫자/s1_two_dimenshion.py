import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = [[0]*N for _ in range(N)]


    change_toggle = [1, -1]         #행렬 인덱스 증감 토글
    change_toggle_switch = False    #True = 감소 False = 증가

    move_count = N      #이동 횟수
    number = 1          #배열 입력값

    row = 0             #초기 위치
    col = -1

    point = 'row'       #이동 포인트

    for idx in range(N*N):
        #제일 위에 행만 N번 이동
        if move_count >= N:         # col = 0, 1, 2, 3, 4
            for idx_col in range(move_count):
                col += change_toggle[change_toggle_switch]  #토글 상태만큼 이동
                result[row][col] = number
                number += 1
            move_count -= 1                                 # 이동 끝나면 이동횟수 감소(가로 이동만)
        else:
            if point == 'col':
                for idx_col in range(move_count):
                    col += change_toggle[change_toggle_switch]
                    result[row][col] = number
                    number += 1
                point = 'row'                                # 가로 이동 끝나면 세로 이동으로 변경
                move_count -= 1                              # 이동 끝나면 이동횟수 감소(가로 이동만)
            else:
                for idx_row in range(move_count):
                    row += change_toggle[change_toggle_switch]
                    result[row][col] = number
                    number += 1
                point = 'col'                                   #세로 이동 끝나면 가로 이동으로 변경
                change_toggle_switch = not change_toggle_switch # 증감 토글 (세로 이동만)

    print('#{}'.format(test_case))

    for row in range(N):
        for col in range(N):
            print(result[row][col], end=" ")
        print()