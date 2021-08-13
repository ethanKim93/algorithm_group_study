import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tot_max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            tot_temp = 0
            for ik in range(i, i+M):
                for jk in range(j, j+M):
                    tot_temp += arr[ik][jk]
            if tot_temp > tot_max:
                tot_max = tot_temp

    print('#{} {}'.format(tc, tot_max))


