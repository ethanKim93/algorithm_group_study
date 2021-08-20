import sys
sys.stdin = open('input.txt')

def is_pal(x):
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
        else:
            return True

def check(boadrd):
    for i in range(100):               # 회문의 길이 고정하는 반복문
        for j in range(100):           # 전체 board의 행과 열을 순회하는 반복문
            for k in range(i+1):       # 회문 여부를 판단할 문자열의 출발 위치 정하는 반복문
                row =''
                col=''
                for l in range(100-i):
                    row += board[j][l-k+i]
                    col += board[l-k+i][j]
                if is_pal(row) or is_pal(col):
                    return '#{} {}'.format(tc, l+1)



for tc in range(1, 11):
    tc = input()
    board = [list(input()) for _ in range(100)]
    check(board)