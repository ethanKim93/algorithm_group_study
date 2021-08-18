import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #길이가 M인 회문 찾기
    arr = [list(input()) for _ in range(N)]
    ans = ''

    #행검사
    for i in range(N):
        for j in range(N-M+1):
            a = arr[i][j:j+M]
            if a == a[::-1]:
                ans = "".join(a)
                print('#{} {}'.format(tc,ans))
    #열검사
    for i in range(N):
        for j in range(N-M+1):
            ams = ''
            for m in range(M):
                ams += arr[j + m][i]
            if ams == ams[::-1]:
                print('#{} {}'.format(tc, ams))