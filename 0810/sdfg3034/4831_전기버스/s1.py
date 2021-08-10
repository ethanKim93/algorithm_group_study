import sys
sys.stdin = open('input.txt')

T=int(input())
for i in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    M_numbers = list(map(int, input().split()))
    road =[1]+[0]*N
    for charger in M_numbers:
        road[charger] += 1
    checker = K
    count = 0
    checker_count=0
    while checker < N:
        if road[checker] == 1:
            count += 1
            checker += K
        else:
            checker -= 1
            checker_count += 1
        if checker_count>N:
            count = 0
            break
    print('#{0} {1}'.format(i,count))