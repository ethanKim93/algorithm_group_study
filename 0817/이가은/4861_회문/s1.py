import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for test in range(T):
    N, M = map(int, input().split())
    palin = [] # 회문

    for n in range(N):
        palin.append(input())

    result = ''
    #가로 회문 탐색
    for i in range(N):
        for j in range(N-M+1):
            if palin[i][j:j+M] == palin[i][j:j+M][::-1]:
                result = palin[i][j:j+M]
                break


    #세로 회문 탐색
    for i in range(N-M+1):
        for j in range(N):
            col_palin = [] #세로 회문 찾아 넣을 list 생성
            for col in range(M):
                col_palin.append(palin[i+col][j])
            if col_palin == col_palin[::-1]:
                result = ''.join(col_palin)
                break


    print('#{} {}'.format(test+1, result))
