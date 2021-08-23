import sys
sys.stdin = open('input.txt')

def sudoku_row(num_list):
    for i in range(9):
        rng = list(range(1, 10))
        for j in range(9):
            if num_list[i][j] in rng:
                rng.remove(num_list[i][j])
            else:
                return 0
    return 1

def sudoku_column(num_list):
    for j in range(9):
        rng = list(range(1, 10))
        for i in range(9):
            if num_list[i][j] in rng:
                rng.remove(num_list[i][j])
            else:
                return 0
    return 1

def sudoku_box(num_list):
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            rng = list(range(1, 10))
            box = []
            for num in [row[j:j+3] for row in num_list[i:i+3]]:
                box += num

            for n in box:
                if n in rng:
                    rng.remove(n)
                else:
                    return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    r = sudoku_row(sudoku)
    c = sudoku_column(sudoku)
    b = sudoku_box(sudoku)

    if r == c == b == 1:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))


    
'''
체크방식으로 가야한다
가로검사와 세로검사, 3X3검사(인덱스의 위치를 잡아(0, 3, 6 --> 가로세로를 3으로 나눴을때 떨어지는 지점 두군데가 겹치는 곳) 체크)
'''

    

