import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int,input().split()))
    cnt = 0
    for i in range(2, L-1):
        for j in range(1, buildings[i]+1):
            if j > buildings[i-1] and j > buildings[i-2] and j>buildings[i+1] and j > buildings[i+2]:
                cnt += 1

    print('#{0} {1}'.format(tc, cnt))
