import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    blank = [[0] * 10 for _ in range(10)]	# 빈 흰종이
    N = int(input())

    cnt = 0  # 겹치는 칸 세주기

    for k in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:  # 컬러가 빨간색이고
                    if blank[x][y] == 0:	# 빈칸이 0이면
                        blank[x][y] = 1		# 빈칸에 1 칠해
                    elif blank[x][y] == 2:	# 빨간색 칠하다가 파란색 나오면
                        blank[x][y] = 3		# 빈칸에 3 칠하고 (보라색)
                        cnt += 1			# 하나 세

                elif color == 2:  # 컬러가 파란색이고
                    if blank[x][y] == 0:	# 빈칸이 0이면
                        blank[x][y] = 2		# 빈칸에 2 칠해
                    elif blank[x][y] == 1:	# 파란색 칠하다가 빨간색 나오면
                        blank[x][y] = 3		# 빈칸에 3칠하고 (보라색)
                        cnt += 1			# 하나 세
    print('#{} {}'.format(tc, cnt))