import sys
sys.stdin = open('input.txt')

def check(word):
    if word == word[::-1]:
        return True
    else:
        return False

for _ in range(1, 11):
    tc = int(input())
    matrix = [list(input()) for _ in range(100)]
    cnt = 0
    row = ''
    col = ''
    for M in range(100, 0, -1):
        if cnt:
            break
        for i in range(100):
            for j in range(100-M+1):  # M 만큼 확인을 해야하므로 row,col의 마지막 숫자는 N-M
                for k in range(M):  # 길이 M의 문자만큼 word에 삽입
                    col += matrix[j+k][i]
                    row += matrix[i][j+k]
                if check(col) or check(row):  # reverse 확인
                    cnt = M
                row = ''
                col = ''
    print('#{} {}'.format(tc, cnt))
