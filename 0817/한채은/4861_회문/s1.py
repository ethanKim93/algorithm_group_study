from pprint import pprint
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    total = []

    palin = []
    for n in range(N):
        palin.append(input())

    # 가로
    for i in range(N):
        for j in range(N - M + 1):
            if palin[i][j:j+M] == palin[i][j:j+M][::-1]:    # 회문이 맞는지 확인하기
                total.append(palin[i][j:j+M])

    # 세로
    for r in range(N - M + 1):
        for c in range(N):
            col_lst = []  # 세로줄
            for i in range(M):  # 세로줄 입력
                col_lst.append(palin[r + i][c])
            if col_lst == col_lst[:: -1]:  # 세로줄이 회문이면
                total.append(''.join(col_lst))

    print('#{} {}'.format(tc, total[0]))

