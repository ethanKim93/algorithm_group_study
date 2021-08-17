import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = []
    ls = []

    for n in range(N):
        row = input()
        ls.append(row)
        for a in range(N-M+1):
            if row[a:M+a] == row[a:M+a][::-1]:
                answer.append(row[a:M+a])
            elif row[0:M+1] == row[0:M+1][::-1]:
                answer.append(row)

    for i in range(N):
        col = []
        joincol = ''
        for j in range(N):
            col.append(ls[j][i])
        joincol = ''.join(col)
        if joincol == joincol[::-1]:
            answer.append(joincol)
            break
        for a in range(N-M+1):
            if joincol[a:M+a] == joincol[a:M+a][::-1]:
                answer.append((joincol[a:M+a]))

    answer = ''.join(answer)
    print('#{} {}'.format(tc, answer))