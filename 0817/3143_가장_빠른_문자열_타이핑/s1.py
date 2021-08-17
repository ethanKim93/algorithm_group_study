import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):

    while True:
        A,B= input().split()
        if 1<=len(A)<=100000 and 1<=len(B)<=100:
            break

    AL=len(A)
    BL=len(B)
    count=0
    for i in range(AL):
        if A[i:i+BL]==B:
            i=i+BL
            count+=1



    total= AL-(count*BL)
    total=total+count
    print('#{} {}'.format(tc, total))




