import sys
sys.stdin = open('input.txt')

def is_pal(x):                                      # 회문 여부 재귀로 확인
    if len(x) > 1:
        if x[0] == x[-1]:
            return is_pal(x[1:-1])
    else:
        return True

def check(board):
    for i in range(100):                            # 회문의 길이 고정하는 반복문
        for j in range(100):                        # 전체 board의 행과 열을 순회하는 반복문
            for k in range(i+1):                    # 회문 여부를 판단할 문자열의 출발 위치 정하는 반복문
                row = ''
                col = ''
                for l in range(100-i):              # 회문의 길이만큼 순회하며 row, col에 문자를 더해줄 반복문
                    row += board[j][l-k+i]          # 행 고정된 상태로 회문의 길이만큼 concatenate 
                    col += board[l-k+i][j]          # 열 고정된 상태로 회문의 길이만큼 concatenate
                if is_pal(row) or is_pal(col):      # 행과 열 중에 회문인 경우라면
                    return l+1                      # 현재 회문의 길이 반환

for tc in range(1,11):
    tc = input()
    board = [input() for _ in range(100)]
    print('#{} {}'.format(tc, check(board)))
