import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n_list = list(map(int,input().split()))

    n = len(n_list) # 원소의 개수
    flag = False
    for i in range(1,1<<n):
        result = 0
        for j in range(n):
            if i&(1<<j):
                result += n_list[j]
        if result == 0:
            flag = True
    if flag:
        print(1)
    else:
        print(0)