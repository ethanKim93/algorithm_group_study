import sys
sys.stdin = open("input.txt")

for _ in range(10):
    test = int(input())

    board = []
    for _ in range(100):
        board.append(str(input()))

    result = []

    # 세로 회문 탐색
    M = 100
    while M > 1:
        for i in range(100 - M + 1):
            for j in range(100):
                col_board = []                           # 세로 회문 찾아 넣을 list 생성
                for col in range(M):
                    col_board.append(board[i + col][j])
                if col_board == col_board[::-1]:
                    result.append(M)
                    break
        if len(result) == 1:                             # 만약 result에 palindrome이 추가되면 더이상 실행하지 않는다.
            break
        M -= 1

    #가로 회문 탐색
    M = 100
    while M > 1 :
        for i in range(100):
            for j in range(100-M+1):
                if board[i][j:j+M] == board[i][j:j+M][::-1]:
                    result.append(M)
                    break
        M -= 1


    print('#{} {}'.format(test,max(result)))