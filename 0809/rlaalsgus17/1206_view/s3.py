import sys

sys.stdin = open('input.txt')

floor = [-2,-1,1,2]

# 0822 재풀이
for tc in range(1, 11):
    N = int(input())
    bulidings = list(map(int,input().split()))

    ans = 0
    for i in range(2,len(bulidings)-2):
        sub_floor = bulidings[i]
        for j in floor:
            if bulidings[i] < bulidings[i+j]:
                break
            if sub_floor > (bulidings[i] - bulidings[i+j]):
                sub_floor = (bulidings[i] - bulidings[i+j])
        else:
            ans += sub_floor
    print('#{0} {1}'.format(tc, ans))
