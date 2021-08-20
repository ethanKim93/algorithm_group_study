import sys
sys.stdin = open("s_input.txt")
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    P = int(input())
    station_arr =[]
    station_count = {}
    for i in range(P):
        c = int(input())
        station_arr.append(c)
        station_count[c] = 0

    for st in station_arr:
       for i in range(a1,b1+1):
           if i == st:
                station_count[st] += 1

       for i in range(a2, b2+1):
           if i == st:
                station_count[st] += 1

    print('#{}'.format(tc),end='')
    for c in station_arr:
        print(' {}'.format(station_count[c]),end='')
    print()