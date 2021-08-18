import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    board = [list(input()) for _ in range(N)]
    flag_i = 0
    flag = 0
    for i in range(N):            #행 검사
        for j in range(N-M+1):
            k = j+M-1
            change_j = j
            counter = 0
            while board[i][change_j] == board[i][k]: #행 검사
                change_j += 1
                k -= 1
                counter += 1
                if counter == M//2:
                    flag_i = i
                    flag_j = j
                    flag = 1
                    break
            while board[change_j][i] == board[k][i]: #열 검사
                change_j += 1
                k -= 1
                counter += 1
                if counter == M//2:
                    flag_j = i
                    flag_i = j
                    flag = 2
                    break
    if flag == 1:
        word = ''.join(board[flag_i][flag_j:flag_j + M])
        print('#{} {}'.format(test_case,word))
    elif flag == 2:
        word = ''
        for i in range(M):
            word +=board[flag_i+i][flag_j]
        print('#{} {}'.format(test_case,word))



