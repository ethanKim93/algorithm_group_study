#정답 못 맞춘..

import sys
sys.studin = open('input.txt', 'r')

def dfs(cnt,num):
    global max_money
    if cnt == N:
        money = "".join(num)
        if money > max_money:
            max_money = money
        return
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if num[i] <= num[j]:
                num[i],num[j] = num[j], num[i]
                str_num = "".join(num)
                if visited.get((str_num,cnt+1),1):
                    visited[(str_num,cnt+1)] = 0
                    dfs(cnt+1,num)
                num[i],num[j] = num[j], num[i]

T = int(input())
for tc in range(1,T+1):
    tmp, N = input().split()
    num = list(tmp)
    N = int(N)
    max_money = "0"
    visited = {}
    dfs(0,num)
    print('#{} {}'.format(tc,max_money))