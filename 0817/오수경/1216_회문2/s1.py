import sys
sys.stdin = open('input.txt')



for tc in range(1, 11):
    T = input()
    board = [list(input()) for _ in range(100)]
    longest = []
    for M in range(100, 2, -1): # 회문의 길이
        for i in board:
            a = 0
            while a + M <= len(i):
                if i[a:a+M] == i[a:a+M][-1::-1]:
                    longest.append(M)
                    break

                else:
                    a += 1

    for i in range(100):
        for j in range(100):
            if i < j:
                board[i][j], board[j][i] = board[j][i], board[i][j]

    for M in range(100, 2, -1): # 회문의 길이
        for i in board:
            a = 0
            while a + M <= len(i):
                if i[a:a+M] == i[a:a+M][-1::-1]:
                    longest.append(M)
                    break

                else:
                    a += 1



    print('#{} {}'.format(tc, max(longest)))