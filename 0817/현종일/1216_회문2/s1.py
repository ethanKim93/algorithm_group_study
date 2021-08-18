import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    field = [input() for _ in range(100)]

    max_leng = 0

    # 가로축 먼저
    for leng in range(100, 0, -1):
        for row in range(100):
            for col in range(100-leng+1):
                if field[row][col:col + leng] == field[row][col:col + leng][::-1] and max_leng < leng:
                    max_leng = leng

        for row in range(100-leng+1):
            for col in range(100):
                match = ''
                for i in range(leng):
                    match += field[row + i][col]
                if match == match[::-1] and max_leng < leng:
                    max_leng = leng

    print('#{} {}'.format(tc, max_leng))





