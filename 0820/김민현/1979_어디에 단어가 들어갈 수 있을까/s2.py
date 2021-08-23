import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())

    #띠를 둘렀을 때
    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+1))
    ans = 0

    for i in range(N+1):
        #행을 검사
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1: #흰색 부분이야
                cnt_r += 1
            else:
                #벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        # 끝까지 가서야 하는 완성이 된 경우(띠를 두르면 필요 없어짐
        # if cnt_r == K:
        #     ans += 1
        # 행을 검사
        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:  # 흰색 부분이야
                cnt_c += 1
            else:
                # 벽이라면
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        # if cnt_c == K:
        #     ans += 1
    print('#{} {}'.format(tc,ans))