
'''
1 2 3 4 5 6 7 8
0 1 0 1 0 0 0 1
0 1 1 1 0 1 0 1
1 0 0 0 1 1 0 1
'''

import sys
sys.stdin = open("input.txt")

N = int(input())
switch = list(map(int,input().split()))
P = int(input())
for _ in range(P):
    gender,std = map(int,input().split())
    if gender == 1:
        for i in range(std-1,N,std):
            if switch[i]: switch[i] = 0
            else: switch[i] = 1
    else:
        k = 0
        while std-k > 0 and std+k < N:
            if switch[std-k-1] == switch[std+k-1]:
                if switch[std-k-1]:
                    switch[std-k-1] = 0
                    switch[std+k-1] = 0
                else:
                    switch[std-k-1] = 1
                    switch[std+k-1] = 1
            else:
                break
            k += 1

for idx in range(1,len(switch)+1):
    print(switch[idx-1],end=' ')
    if not idx%20:
        print()