import sys
sys.stdin = open("input.txt")
'''
1의 개수를 누적시켜서 K가 됬을 때,
1 ) 다음 수가 0 이면 total +=1
2 ) 끝에 도달하면, 즉 루프 하나가 끝나면 total += 1
'''
for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    
    for i in range(N):
        cnt1 = 0 
        cnt2 = 0
        for j in range(N):
            if puzzle[i][j]:
                cnt1 += 1
            else:
                if cnt1 == K:
                    total += 1
                cnt1 = 0
            
            if puzzle[j][i]:
                cnt2 += 1
            else:
                if cnt2 == K:
                    total += 1
                cnt2 = 0

        if cnt1 == K:
            total += 1
        if cnt2 == K:
            total += 1
    print('#{} {}'.format(tc, total))


