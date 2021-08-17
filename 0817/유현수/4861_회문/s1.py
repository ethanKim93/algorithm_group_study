import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = []
    for i in range(N):
        words.append(input())

    result = ''

    # 가로 회문 탐색
    for i in range(N):
        for j in range(N-M+1):
            if words[i][j:j+M] == words[i][j:j+M][::-1]:
                result = words[i][j:j+M]
                break

    # 세로 회문 탐색
    for i in range(N):
        for j in range(N-M+1):
            word = ''
            for k in range(M):
                word += words[j + k][i]
            if word == word[::-1]:
                result = word
                break

    print('#{} {}'.format(tc, result))
