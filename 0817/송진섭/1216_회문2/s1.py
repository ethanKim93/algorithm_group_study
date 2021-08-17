import sys
sys.stdin = open('input.txt')


def search_palindrome(N, M, word_list):
    for i in range(N):
        for j in range(N-M+1):
            row_word = col_word = ''
            for k in range(M):
                row_word += word_list[i][j+k]
                col_word += word_list[j+k][i]
            if row_word == row_word[::-1]:
                return row_word
            elif col_word == col_word[::-1]:
                return col_word
    return False


for _ in range(10):
    tc = input()
    word_list = [list(input()) for _ in range(100)]
    for M in range(100, -1, -1):  # 100부터 역순으로 찾는 범위를 줄인다
        if search_palindrome(100, M, word_list):
            print('#{} {}'.format(tc, M))
            break  # 회문을 찾으면 출력 후 종료