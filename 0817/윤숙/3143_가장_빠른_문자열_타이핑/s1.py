import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):


    A,B= input().split()


    AL=len(A)
    BL=len(B)
    count=0
    idx=0
    while idx < len(A):
        if A[idx:idx+BL]==B:
            idx=idx+BL
        else:
            idx+=1
        count+=1


    print('#{} {}'.format(tc, count))




