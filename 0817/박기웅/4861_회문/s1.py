import sys
sys.stdin = open("sample_input.txt")
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    str2d = [input() for _ in range(N)]
    str2d_tr = [x for x in zip(*str2d)] #방향 전환 string -> list(tuple) 형태

    ans = ''
    ans_tr = ()
    for i in range(N):
        for j in range(N-M+1):
            # 가로 확인 루프 for-else 구문
            for k in range(j, (j+j+M)//2):
                if str2d[i][k] != str2d[i][j+j+M-k-1]:
                    break # 회문이 아니면 나감
            else:
                ans = str2d[i][j:j+M+1]
                break # 회문 찾으면 나감
            # 세로 확인 루프
            for k in range(j, (j+j+M)//2):
                if str2d_tr[i][k] != str2d_tr[i][j+j+M - k - 1]:
                    break
            else:
                ans_tr = str2d_tr[i][j:j+M+1]
                break
        if ans or ans_tr:
            break #회문 찾은 경우 마지막 루프까지 나감

    print('#{} {}'.format(tc, ans if ans else ''.join(map(str, ans_tr))))
