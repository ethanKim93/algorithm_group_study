import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bat = []
    for _ in range(N):
        bat_s = input()
        bat.append(bat_s)
    a = N//2
    answer = 0
    for i in range(N):
        if i <= a:
            for j in range(a-i,a+i+1):
                answer += int(bat[i][j])
        else:
            for j in range(a-N+i+1,a+N-i):
                answer += int(bat[i][j])
    print('#{} {}'.format(tc,answer))