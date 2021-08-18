import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    for row in range(N):  # 가로 확인
        for col in range(N-M+1):  # M 만큼 확인을 해야하므로 col의 마지막 숫자는 N-M
            if matrix[row][col:col+M] == matrix[row][col:col+M][::-1]:  # reverse 확인
                print('#{} {}'.format(tc, ''.join(matrix[row][col:col+M])))
                break
    else: # 세로 확인
        word = ''
        for col in range(N):
            for row in range(N-M+1):  # M 만큼 확인을 해야하므로 row의 마지막 숫자는 N-M
                for k in range(M):  # 길이 M의 문자만큼 word에 삽입
                    word += matrix[row+k][col]
                if word == word[::-1]:  # reverse 확인
                    print('#{} {}'.format(tc, word))
                    break
                else:
                    word = ''








