"""
N-> 1번 부터 N번까지
Q-> Q회동안
i->값
L번 상자부터 R번까지 값을 i로 변경

1   // Test Case 개수
5 2 // 첫 번째 Test Case, N=5, Q=2
1 3 // i = 1일 때, L=1, R=3
2 4	// i = 2일 때, L=2, R=4


"""

import sys
sys.stdin=open('input.txt')

T=int(input())

for tc in range(1,T+1):
    arr_N,round=map(int,input().split())

    L=[0]*round
    R=[0]*round
    Box=[0]*arr_N


    for j in range(round):
        L, R = map(int, input().split())
        for i in range(L-1,R):
            Box[i]=L


    Box=" ".join(map(str,Box))
    print('#{} {}'.format(tc,Box))

